from Tools.scripts.ndiff import fail
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def verificando_campos(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'name')))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'email')))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'password')))

def click_cadastro(driver):
    senha = driver.find_element_by_id('password')
    senha.click()
    senha.send_keys(Keys.TAB)
    senha.send_keys(Keys.ENTER)

def verificando_alerta(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div/div/div/div[2]/form/div[1]/p')))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div/div/div/div[2]/form/div[2]/p')))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                     '/html/body/div/div/div/div[2]/form/div[3]/p')))


