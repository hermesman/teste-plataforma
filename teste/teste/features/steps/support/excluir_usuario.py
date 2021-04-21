from Tools.scripts.ndiff import fail
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def clico_excluir(driver):
    excluir = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table/tr/td[4]/a')
    excluir.click()
    time.sleep(10)

def usuario_exluido(driver):
    clicando_fora = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/h2[1]')
    clicando_fora.click()
    driver.execute_script('window.scrollBy(0, 250)')
    assert not len(driver.find_elements_by_id("tdUserName1"))






