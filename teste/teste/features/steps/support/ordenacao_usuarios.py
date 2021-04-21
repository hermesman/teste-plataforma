from Tools.scripts.ndiff import fail
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from support import usuario
from support import obrigatoriedade_campos
import time

def verifico_lista_usuarios(driver):
    usuario.informo_campos_obrigatorios(driver)
    obrigatoriedade_campos.click_cadastro(driver)
    nome = driver.find_element_by_id("name")
    nome.send_keys('Maria da Silva')
    email = driver.find_element_by_id("email")
    email.send_keys('maria.silva@teste.com')
    senha = driver.find_element_by_id("password")
    senha.send_keys('12345678')
    senha.send_keys(Keys.TAB)
    senha.send_keys(Keys.ENTER)
    nome = driver.find_element_by_id("name")
    nome.send_keys('Francisca da Silva')
    email = driver.find_element_by_id("email")
    email.send_keys('francisca.silva@teste.com')
    senha = driver.find_element_by_id('password')
    senha.send_keys('12345678')
    senha.send_keys(Keys.TAB)
    senha.send_keys(Keys.ENTER)

def lista(driver):
    assert len(driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/table/tr[1]/td[1]"))
    assert len(driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/table/tr[2]/td[1]"))
    assert len(driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/table/tr[3]/td[1]"))






