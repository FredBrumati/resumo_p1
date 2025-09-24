import pytest
from exemplo3 import Aluno, Professor

def test_media_e_status():
    aluno = Aluno("Pedro", 16)
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(4)
    assert aluno.media() == 6
    assert aluno.status() == "Aprovado"

def test_professor_atribui_nota():
    aluno = Aluno("Pedro", 16)
    prof = Professor("Carla", 35)
    msg = prof.atribuir_nota(aluno, 9)
    assert msg == "Carla atribuiu nota 9 para Pedro."
    assert aluno.notas == [9]

def test_aluno_reprovado():
    aluno = Aluno("Ana", 17)
    aluno.adicionar_nota(3)
    aluno.adicionar_nota(5)
    assert aluno.media() == 4
    assert aluno.status() == "Reprovado"

def test_info():
    aluno = Aluno("Pedro", 16)
    prof = Professor("Carla", 35)
    assert aluno.info() == "Nome: Pedro | Idade: 16"
    assert prof.info() == "Nome: Carla | Idade: 35"
