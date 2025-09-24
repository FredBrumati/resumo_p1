import pytest
from exemplo4 import *

usuario_autorizado = {"nome": "Ana", "autorizado": True}
usuario_nao_autorizado = {"nome": "João", "autorizado": False}

def test_ver_dados_autorizado():
    assert ver_dados(usuario_autorizado) == "Dados confidenciais"

def test_editar_dados_autorizado():
    assert editar_dados(usuario_autorizado) == "Dados editados com sucesso"

def test_ver_dados_nao_autorizado():
    with pytest.raises(PermissionError):
        ver_dados(usuario_nao_autorizado)
