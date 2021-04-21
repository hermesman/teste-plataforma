from Tools.scripts.ndiff import fail
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def informo_senha_incorreta(driver):
    senha = driver.find_element_by_id('password')
    senha.send_keys('1234567')

def alerta_senha_errado(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div/div/div/div[2]/form/div[3]/p')))


