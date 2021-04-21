from Tools.scripts.ndiff import fail
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def verificando_campos(driver):
    time.sleep(5)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'name')))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'email')))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'password')))

def verificando_campos_vazios(driver):
    nome = driver.find_element_by_id('name').text
    email = driver.find_element_by_id('email').text
    senha = driver.find_element_by_id('password').text
    assert nome == ''
    assert email == ''
    assert senha == ''


