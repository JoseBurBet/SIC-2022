from selenium import webdriver

driver = webdriver.Edge(executable_path='./msedgedriver.exe')
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://web.whatsapp.com/")

print("Session ID 1: " + session_id)
print("Executor URL: " + executor_url)


with open("./whatsapp_session.txt", "w") as text_file:
    text_file.write("{}\n".format(executor_url))
    text_file.write(session_id)
