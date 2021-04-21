from Tools.scripts.ndiff import fail
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def informo_campos_obrigatorios(driver):
    nome = driver.find_element_by_id('name').send_keys('João da Silva')
    email = driver.find_element_by_id('email').send_keys('joao.silva@teste.com')
    senha = driver.find_element_by_id('password').send_keys('12345678')


def exibir_lista_usuario(driver):
    clicando_fora = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/h2[1]')
    clicando_fora.click
    driver.execute_script('window.scrollBy(0, 250)')
    nome_lista = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "tdUserName1")))
    email_lista = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "tdUserEmail1")))





