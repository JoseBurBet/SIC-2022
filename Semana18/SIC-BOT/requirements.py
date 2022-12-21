# Samsung innovation campus
# by: Profe Jose
# python version : 3.9.12
# libraries:

    #keras                         2.10.0
    #Keras-Preprocessing           1.1.2
    #nltk                          3.7
    #numpy                         1.21.5
    #tensorflow                    2.10.1
    #tensorflow-estimator          2.10.0
    #tensorflow-io-gcs-filesystem  0.27.0
    
def start():
    #intalacion en jupyter
    #import sys 
    #!{sys.executable} -m pip install tensorflow
    #!{sys.executable} -m pip install keras
    #!{sys.executable} -m pip install nltk
    
    
#__________________________ de aqui para abajo en consola______________
    
    import pip
    
    
    #pip.main(["list"])

    pip.main(["install","numpy==1.21.5"])
    pip.main(["install","nltk==3.7"])
    pip.main(["install","tensorboard==2.10.1"])
    pip.main(["install","tensorflow-estimator==2.10.0"])
    pip.main(["install","keras==2.10.0"])
    pip.main(["install","Keras-Preprocessing==1.1.2"])
    pip.main(["install","tensorflow==2.10.1"])
    pip.main(["install","selenium"])


    

    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('universal_tagset')
    nltk.download('spanish_grammars')
    nltk.download('tagsets')
    nltk.download('stopwords') # faltaaaaa
    nltk.download('omw-1.4') #faltaaaa

        
    
# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    start()
