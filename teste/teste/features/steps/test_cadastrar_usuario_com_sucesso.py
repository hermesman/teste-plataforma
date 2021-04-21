from support import usuario
from support import obrigatoriedade_campos
from behave import *

@Given("que acesso a página do sistema #6")
def acesso_a_pagina(context):
   context.chrome.maximize_window()

@Given("informo campos obrigatórios")
def informo_campos(context):
    usuario.informo_campos_obrigatorios(context.chrome)

@When("clico em cadastrar #7")
def cadastrar(context):
    obrigatoriedade_campos.click_cadastro(context.chrome)

@Then("deve exibir lista com usuários cadastrados")
def lista_usuarios(context):
    usuario.exibir_lista_usuario(context.chrome)
