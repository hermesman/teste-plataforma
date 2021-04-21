from Tools.scripts.ndiff import fail
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def nao_informo_sobrenome_campo(driver):
    nome = driver.find_element_by_id('name')
    nome.send_keys('João')

def alerta_nome_completo(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div/div/div/div[2]/form/div[1]/p')))


