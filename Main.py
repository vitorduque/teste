from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\LabInfo\Documents\\selenium_github-main\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('file:///C:/Users/LabInfo/Downloads/cadastro.html')
    print("o teste 1 foi um sucesso!")
    def enviarDados(nome, email, telefone, data):
        nome_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nome"))
        ) 
        print("o teste 2 foi um sucesso!")
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        print("o teste 3 foi um sucesso!")
        telefone_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "numero"))
        )
        print("o teste 4 foi um sucesso!")
        data_login = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, "data"))
        )
        print("o teste 5 foi um sucesso!")
        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "botao"))
        )
        print("o teste 6 foi um sucesso!")
        nome_login.send_keys(nome)
        print("o teste 7 foi um sucesso!")
        email_login.send_keys(email)
        print("o teste 8 foi um sucesso!")
        telefone_login.send_keys(telefone)
        print("o teste 9 foi um sucesso!")
        data_login.send_keys(data)
        print("o teste 10 foi um sucesso!")
        btn_login.click()
        print("o teste 11 foi um sucesso!")
    alert = enviarDados('ApenasUmDio','blablabla@gmail.com', "32147238", '10/03/1975')
    print("o teste foi um sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()