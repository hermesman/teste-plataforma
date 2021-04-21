from support import validar_nome
from support import obrigatoriedade_campos
from behave import *

@Given("que acesso a página do sistema #3")
def acesso_a_pagina(context):
   context.chrome.maximize_window()

@Given("não informo o campo Nome com sobrenome")
def nao_informo_sobrenome(context):
    validar_nome.nao_informo_sobrenome_campo(context.chrome)

@When("clico em cadastrar #2")
def cadastrar(context):
    obrigatoriedade_campos.click_cadastro(context.chrome)

@Then("deve exibir alerta de Nome Completo")
def alerta_nome(context):
    validar_nome.alerta_nome_completo(context.chrome)
