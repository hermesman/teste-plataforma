from support import verificar_campos
from behave import *

@Given("que acesso a página do sistema")
def acesso_a_pagina(context):
   context.chrome.maximize_window()


@When("verifico os campos")
def verificando(context):
    verificar_campos.verificando_campos(context.chrome)

@Then("devem estar vazios")
def campos_vazios(context):
    verificar_campos.verificando_campos_vazios(context.chrome)
