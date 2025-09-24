import pytest
from exemplo3 import Aluno, Professor

def test_media_e_status():
    aluno = Aluno("Pedro")
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(4)
    assert aluno.media() == 6
    assert aluno.status() == "Aprovado"

def test_professor_atribui_nota():
    aluno = Aluno("Pedro")
    prof = Professor("Carla")
    msg = prof.atribuir_nota(aluno, 9)
    assert msg == "Carla atribuiu nota 9 para Pedro."
    assert aluno.notas == [9]
