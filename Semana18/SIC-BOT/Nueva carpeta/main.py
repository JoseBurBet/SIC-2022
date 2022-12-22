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
    #sleep(30)
    print(driver.find_elements(By.CLASS_NAME,"zaKsw"))
    #test=0
    if len(driver.find_elements(By.CLASS_NAME,"zaKsw")) == 0: #cuando ninguno esta abierto (ventana de la derecha)
        print("CHAT ABIERTO")
        message = identificar_mensaje()
        
        if message != None:
            return True
    else:
    chats = driver.find_elements(By.NAME,"_10e6M") # el cuadro del primer chat a la izquierda

    for chat in chats:
        print("DETECTANDO MENSAJES SIN LEER")

        chats_mensajes = chat.find_elements(By.NAME,"_1pJ9J") # el circulo de mensaje no leido

        if len(chats_mensajes) == 0:
            print("CHATS ATENDIDOS")
            continue

        chat.click()
        return True
    return False



# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    whatsapp_bot_init()
    buscar_chats()
