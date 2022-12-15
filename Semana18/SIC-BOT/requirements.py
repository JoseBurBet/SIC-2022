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
    import sys 
    !{sys.executable} -m pip install tensorflow
    !{sys.executable} -m pip install keras
    !{sys.executable} -m pip install nltk
    
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
