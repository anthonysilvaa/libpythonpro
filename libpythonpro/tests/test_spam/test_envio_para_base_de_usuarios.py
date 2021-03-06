from unittest.mock import Mock

import pytest
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    "usuarios",
    [
        [
            Usuario(nome="Anthony", email="anthony@python.pro.br"),
            Usuario(nome="Luciano", email="luciano@python.pro.br")
        ],
        [
            Usuario(nome="Luciano", email="luciano@python.pro.br")
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):

    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'anthony@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Anthony", email="anthony@python.pro.br")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'anthony@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        "anthony@python.pro.br",
        "anthony@python.pro.br",
        "Curso Python Pro",
        "Confira os módulos fantásticos"
    )
