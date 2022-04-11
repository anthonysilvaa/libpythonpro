from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Anthony')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome="Anthony"), Usuario(nome="Renzo")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
