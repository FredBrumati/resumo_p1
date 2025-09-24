"""Exercício 5 – Transporte com Combustível
Implemente um sistema de transportes em Python utilizando classes abstratas:
Crie uma classe abstrata Transporte com atributos capacidade e combustivel.
Essa classe deve possuir os seguintes métodos:
Um método abstrato mover(distancia), que será definido pelas subclasses.
Um método info(), que retorna informações do transporte.
Um método abastecer(litros), que adiciona combustível.
Um método status_combustivel(), que mostra o combustível disponível.
Crie as subclasses:
Carro, que implementa mover(distancia) reduzindo combustível proporcional à distância (1L a cada 10km).
Bicicleta, que implementa mover(distancia) sem gastar combustível, mas aumentando um atributo desgaste.
No programa principal, crie um carro e uma bicicleta, execute movimentos e teste os métodos."""

from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, capacidade):
        self.capacidade = capacidade

    @abstractmethod
    def mover(self, distancia):
        pass

    def info(self):
        return f"Capacidade: {self.capacidade}"

class Carro(Transporte):
    def __init__(self, capacidade, combustivel):
        super().__init__(capacidade)
        self.combustivel = combustivel  # em litros

    def mover(self, distancia):
        consumo = distancia * 0.1  # 0.1 litro por km
        if consumo <= self.combustivel:
            self.combustivel -= consumo
            return f"Carro andou {distancia}km. Combustível restante: {self.combustivel:.1f}L"
        return "Combustível insuficiente!"

    def abastecer(self, litros):
        self.combustivel += litros
        return f"Abastecido {litros}L. Total: {self.combustivel:.1f}L"

class Bicicleta(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)
        self.desgaste = 0

    def mover(self, distancia):
        self.desgaste += distancia * 0.05
        return f"Bicicleta andou {distancia}km. Nível de desgaste: {self.desgaste:.1f}"

# Teste
carro = Carro(5, 10)
bike = Bicicleta(1)

print(carro.info())
print(carro.mover(50))
print(carro.abastecer(5))
print(bike.mover(20))
