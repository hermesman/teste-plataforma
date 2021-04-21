from selenium.webdriver import Chrome


def before_scenario(context, scenario):
    context.chrome = Chrome(
        executable_path='C:\\Users\\MiniSauron\\Downloads\\teste\\teste\\features\\steps\\driver\\chromedriver.exe')
    context.chrome.get('http://prova.stefanini-jgr.com.br/teste/qa/')
    context.chrome.maximize_window()

def after_scenario(context, scenario):
    context.chrome.delete_all_cookies()
    context.chrome.quit()

