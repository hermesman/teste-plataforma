from support import obrigatoriedade_campos
from behave import *

@Given("que acesso a página do sistema #2")
def acesso_a_pagina(context):
   context.chrome.maximize_window()

@Given("não preencho os campos")
def nao_preencho_campos(context):
    obrigatoriedade_campos.verificando_campos(context.chrome)

@When("clico em cadastrar")
def cadastrar(context):
    obrigatoriedade_campos.click_cadastro(context.chrome)

@Then("deve exibir alerta de obrigatoriedade")
def alerta_obrigatoriedade(context):
    obrigatoriedade_campos.verificando_alerta(context.chrome)
