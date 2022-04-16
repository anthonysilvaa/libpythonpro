import pytest
from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['anthony@devpro.com.br', 'renzo@pythonpro.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'felipe@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossun aberta'
    )

    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'anthony']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'felipe@python.pro.br',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossun aberta'
        )



