from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
import re # para limpiar los string
from unicodedata import normalize #normalizar caracteres del español
from selenium.webdriver.common.by import By

filepath = "./whatsapp_session.txt"
driver = webdriver

def crear_driver_session():

    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            if cnt == 0:
                executor_url = line
            if cnt == 1:
                session_id = line

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)
                
    org_command_execute = RemoteWebDriver.execute

    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    RemoteWebDriver.execute = org_command_execute

    return new_driver


def whatsapp_bot_init():
    global driver
    driver = crear_driver_session()


def buscar_chats():
    print("BUSCANDO CHATS")
    sleep(5)
    #print(driver.find_elements(By.CLASS_NAME,"zaKsw"))
    print(len(driver.find_elements(By.CLASS_NAME,"_1RAKT")))
    # si la longitud es 0 es porque tengo chat abierto, si es dif de 0 es porque  no hay chat abierto
    if len(driver.find_elements(By.CLASS_NAME,"zaKsw")) == 0: #cuando ninguno esta abierto (ventana de la derecha)
        
        print("CHAT ABIERTO")
        message = identificar_mensaje()
                                
        if message != None:
            return True
    else:
        #chats = driver.find_elements(By.NAME,"_1Oe6M")
        chats = driver.find_elements(By.CLASS_NAME,"_1Oe6M") # el cuadro del primer chat a la izquierda
                
        #print("len chats: ",len(chats))
        for chat in chats:
            print("DETECTANDO MENSAJES SIN LEER")

            chats_mensajes = chat.find_elements(By.CLASS_NAME,"_1pJ9J") # el circulo de mensaje no leido
            #print("mensajes sin leer: ",len(chats_mensajes))
            #print(chat)
            if len(chats_mensajes) == 0:
                print("CHATS ATENDIDOS")
                continue
            else:
                #print("else")
                chat.click() # abre el chat
                return True
    return False

        # pruebas del profe, ignoren esto :v
        #chats = driver.find_elements(By.CLASS_NAME,"_3uIPm WYyr1")
        #chats = driver.find_elements(By.CLASS_NAME,"_3Bc7H _20c87")
        #chats = driver.find_elements(By.CLASS_NAME,"lhggkp7q ln8gz9je rx9719la")
        #chats = driver.find_elements(By.CLASS_NAME,"_3GlyB")
    



# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    whatsapp_bot_init()
    buscar_chats()
