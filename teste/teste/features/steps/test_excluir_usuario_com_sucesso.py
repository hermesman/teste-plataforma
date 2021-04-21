from support import usuario
from support import excluir_usuario
from support import obrigatoriedade_campos
from behave import *

@Given("que acesso a página do sistema #7")
def acesso_a_pagina(context):
   context.chrome.maximize_window()

@Given("verifico a lista de usuários cadastrados")
def informo_campos(context):
    usuario.informo_campos_obrigatorios(context.chrome)
    obrigatoriedade_campos.click_cadastro(context.chrome)
    usuario.exibir_lista_usuario(context.chrome)

@When("clico em Excluir")
def excluir(context):
    excluir_usuario.clico_excluir(context.chrome)

@Then("o usuário deve ser excluído da lista")
def usuario_deve_ser_excluido_lista(context):
    excluir_usuario.usuario_exluido(context.chrome)

