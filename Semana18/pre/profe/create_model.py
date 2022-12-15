import json
import pickle
import numpy as np

import nltk

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense,Dropout
from tensorflow.keras.optimizers import SGD
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('spanish')

ignore_words=["?","¿","!","¡"]
data_file= open("intents.json").read() #aqui cargo el archivo en formato json
intents = json.loads(data_file) # aqui convierto el archivo json a diccionario
intents

############################# creo las referencias a partir de intents #########################################

def references():

    words=[]
    classes=[]
    documents=[]

    for intent in intents["intents"]: #accedo a la lista de diccionarios
        for pattern in intent["patterns"]: # accedo a la lista de palabraas
            
            
            #tokenizar cada palabra
            
            w=nltk.word_tokenize(pattern) #separamos las oraciones palabra por palabra y guardamos cada palabra como token
            words.extend(w)
            
            #agrego un array de documentos
            documents.append((w,intent["tag"]))
            
            #añadimos clases  a nuestra lista de clases
            if intent["tag"] not in classes:
                classes.append(intent["tag"])

    return words,classes,documents
################################################## tokenizar y lematizar ##########################

def lematizer(words,classes,documents):

    stemmer = SnowballStemmer('spanish')
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]

    pickle.dump(words,open("words.pkl","wb"))
    pickle.dump(classes,open("classes.pkl","wb"))


########################################## preparacion de la red neuronal (datos de entrenamiento) #######################

def pre_training(words,classes,documents):

    training=[]
    output_empty=[0]*len(classes)# creamos una matriz del numero de patterns con valor inicial 0
                                # creamos una matriz que tenga tantas columnas como classes

    for doc in documents: #en doc esta la raw_data -> datos sin procesar
    #doc[0] -> tokens, o palabras
    #doc[1] -> tag -> clase
        
        
        #bag of words
        bag=[]
        #lista de tokens
        pattern_words=doc[0]# doc[0] es la lista de palabras
        # lematizacion del token

        pattern_words= [stemmer.stem(word.lower()) for word in pattern_words  if word not in ignore_words ]
        
        
        # si la palabra coincide introduzco 1, en caso contrario 0
        
        for palabra in words:
            bag.append(1) if palabra in pattern_words else bag.append(0) 
            #si la palabra de referencia esta dentro de pattern_words ponga 1
            #print(bag)
        
        output_row =list(output_empty)
        output_row[classes.index(doc[1])] = 1 #doc en la posicion 1 es el pattern
                    #busca en que posicion esta el tag y pone un 1 en esa posicion del output_row
                    #ejemplo si es saludo pone [1,0,0,0]
        
        training.append([bag,output_row])
      


    training=np.array(training) # cambiamos la lista de listas a un formato numpy.array

    x_train= list(training[:,0]) #asi porque estamos en formato numpy.array ||| training[inicio:fin,index]
    y_train= list(training[:,1])

    return x_train,y_train

################################ Creacion del modelo #################################

def create_model(x_train,y_train):

    model = Sequential()
                    
    #añadimos capas a la red
    model.add(Dense(128, input_shape=(len(x_train[0]),), activation='relu')) #añadimos 1 capa: entrada de datos
    #model.add(Dense(128, input_shape=(x_train.shape[1],), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64,activation='relu')) #capa oculta -> aprendizaje
    model.add(Dropout(0.5))
    model.add(Dense(len(y_train[0]),activation='softmax')) # capa de salida toma de desiciones

    sgd=SGD(learning_rate=0.01,decay=1e-6,momentum=0.9,nesterov=True) 
    #import tensorflow as tf
    #sgd = tf.keras.optimizers.legacy.SGD(learning_rate=0.1, momentum=0.9)

    model.compile(loss="categorical_crossentropy",optimizer=sgd,metrics=["accuracy"])

    #le mando los datos de train para que entrene y aprenda
    #fit ajusta los datos para crear un modelo (Sequential de 3 capas) que pueda predecir los datos

    hist=model.fit(np.array(x_train),np.array(y_train),epochs=300,batch_size=5,verbose=1)
    model.save("chatbot_model.h5",hist)
    print("modelo creado")

def start_model():
    
    words,classes,documents=references()
    lematizer(words,classes,documents)
    x_train,y_train=pre_training(words,classes,documents)
    create_model(x_train,y_train)



# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    start_model()


