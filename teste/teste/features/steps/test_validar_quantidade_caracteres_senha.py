from support import validar_senha
from support import obrigatoriedade_campos
from behave import *

@Given("que acesso a página do sistema #5")
def acesso_a_pagina(context):
   context.chrome.maximize_window()

@Given("informo senha com 7 caracteres")
def informo_senha_com_sete_caracteres(context):
    validar_senha.informo_senha_incorreta(context.chrome)

@When("clico em cadastrar #4")
def cadastrar(context):
    obrigatoriedade_campos.click_cadastro(context.chrome)

@Then("deve exibir alerta para inserir uma senha com pelo menos 8 caracteres")
def alerta_senha(context):
    validar_senha.alerta_senha_errado(context.chrome)
