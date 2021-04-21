#language: pt

Funcionalidade: Teste no site

Cenário: Validar campos vazios

Dado que acesso a página do sistema
Quando verifico os campos
Então devem estar vazios

Cenário: Validar obrigatoriedade dos campos

Dado que acesso a página do sistema #2
E não preencho os campos
Quando clico em cadastrar
Então deve exibir alerta de obrigatoriedade

Cenário: Validar obrigatoriedade de Nome Completo

Dado que acesso a página do sistema #3
E não informo o campo Nome com sobrenome
Quando clico em cadastrar #2
Então deve exibir alerta de Nome Completo

Cenário: Validar Email

Dado que acesso a página do sistema #4
E não informo o email com padrão “texto@texto.com”
Quando clico em cadastrar #3
Então deve exibir alerta para inserir um email válido

Cenário: Validar quantidade mínima de caracteres no campo Senha

Dado que acesso a página do sistema #5
E informo senha com 7 caracteres
Quando clico em cadastrar #4
Então deve exibir alerta para inserir uma senha com pelo menos 8 caracteres

Cenário: Cadastrar usuário com sucesso

Dado que acesso a página do sistema #6
E informo campos obrigatórios
Quando clico em cadastrar #7
Então deve exibir lista com usuários cadastrados

Cenário: Excluir usuário com sucesso

Dado que acesso a página do sistema #7
E verifico a lista de usuários cadastrados
Quando clico em Excluir
Então o usuário deve ser excluído da lista

Cenário: Validar ordenação de lista dos Usuários Cadastrados

Dado que acesso a página do sistema #8
Quando verifico a lista de usuários cadastrados
Então os usuários devem ser listados pelo ID de forma crescente

Cenário: Validar ordenação de lista dos Usuários Cadastrados após exclusão de linha

Dado que acesso a página do sistema #9
E verifico a lista de usuários cadastrados #2
Quando excluo um usuário
Então os usuários devem ser listados com o mesmo ID


