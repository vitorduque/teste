from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\LabInfo\Documents\\selenium_github-main\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('C:\\Users\\LabInfo\\Downloads\\index.html')
    print("o teste 1 foi um sucesso!")
    def enviarDados(nome, email, cpf, numero):
        nome_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nome"))
        ) 
        print("o teste 2 foi um sucesso!")
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email1"))
        )
        print("o teste 3 foi um sucesso!")
        cpf_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cpf"))
        )
        print("o teste 4 foi um sucesso!")
        numero_login = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, "numero"))
        )
        print("o teste 5 foi um sucesso!")
        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/button"))
        )
        print("o teste 6 foi um sucesso!")
        nome_login.send_keys(nome)
        print("o teste 7 foi um sucesso!")
        email_login.send_keys(email)
        print("o teste 8 foi um sucesso!")
        cpf_login.send_keys(cpf)
        print("o teste 9 foi um sucesso!")
        numero_login.send_keys(numero)
        print("o teste 10 foi um sucesso!")
        btn_login.click()
        print("o teste 11 foi um sucesso!")
    alert = enviarDados('ApenasUmDio','blablabla@gmail.com', "966960234", '32988234290')
    print("o teste foi um sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()
