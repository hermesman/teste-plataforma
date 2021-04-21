from support import verificar_email
from support import obrigatoriedade_campos
from behave import *

@Given("que acesso a página do sistema #4")
def acesso_a_pagina(context):
   context.chrome.maximize_window()

@Given("não informo o email com padrão “texto@texto.com”")
def nao_informo_email_no_padrao(context):
    verificar_email.nao_informo_email_correto(context.chrome)

@When("clico em cadastrar #3")
def cadastrar(context):
    obrigatoriedade_campos.click_cadastro(context.chrome)

@Then("deve exibir alerta para inserir um email válido")
def alerta_email(context):
    verificar_email.alerta_email_errado(context.chrome)
