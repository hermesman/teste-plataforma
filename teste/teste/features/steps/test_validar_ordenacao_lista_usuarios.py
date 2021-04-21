from support import usuario
from support import ordenacao_usuarios
from support import obrigatoriedade_campos
from behave import *

@Given("que acesso a página do sistema #8")
def test_acesso_a_pagina(context):
   context.chrome.maximize_window()

@When("verifico a lista de usuários cadastrados")
def test_verifico_lista(context):
    ordenacao_usuarios.verifico_lista_usuarios(context.chrome)


@Then("os usuários devem ser listados pelo ID de forma crescente")
def test_usuario_deve_ser_excluido_lista(context):
    ordenacao_usuarios.lista(context.chrome)

