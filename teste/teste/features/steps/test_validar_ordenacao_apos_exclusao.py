from support import ordenacao_usuarios
from support import ordenacao_pos_exclusao
from behave import *

@Given("que acesso a página do sistema #9")
def acesso_a_pagina(context):
   context.chrome.maximize_window()

@Given("verifico a lista de usuários cadastrados #2")
def verifico_lista(context):
    ordenacao_pos_exclusao.verifico_lista_usuarios(context.chrome)

@When("excluo um usuário")
def excluo_um_usuario(context):
    ordenacao_pos_exclusao.excluir(context.chrome)

@Then("os usuários devem ser listados")
def usuario_deve_ser_excluido_lista(context):
    ordenacao_pos_exclusao.lista(context.chrome)

@Then("os usuários devem ser listados com o mesmo ID")
def usuario_deve_ser_excluido_lista(context):
    ordenacao_pos_exclusao.lista(context.chrome)

