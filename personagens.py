#Aluno: Yan dos Santos Teixeira M: 2023010
import random

class Personagem:
    def __init__(self, nome, historico=None, energia=10):
        self.nome = nome
        self.energia = energia
        self.historico_batalhas = historico if historico is not None else []

    def incremento(self, quantidade):
        self.energia = min(self.energia + quantidade, 10)

    def decremento(self, quantidade):
        self.energia -= quantidade
        if self.energia <= 0:
            print(f"{self.nome} foi derrotado!")
            self.energia = 0

    def registrar_batalha(self, resultado):
        self.historico_batalhas.append(resultado)

    def sorteio(self):
        return random.randint(1, 6)

    def __str__(self):
        return (f"Nome: {self.nome}, Energia: {self.energia}, "
                f"Histórico de Batalhas: {self.historico_batalhas}")

class Mocinho(Personagem):
    #alimentar o mocinho
    def alimentar(self):
        if self.energia <= 0:
            print(f"{self.nome} está morto e não pode ser alimentado.")
        else:
            self.incremento(2)
            print(f"{self.nome} foi alimentado e ganhou 2 pontos de energia.")
    def alimentar(self):
        quantidade = random.randint(1, 3)
        self.incremento(quantidade)
        print(f"{self.nome} se alimentou e ganhou {quantidade} de energia.")

    #luta do heroi
    def lutar(self, vilao):
        print(f"{self.nome} está lutando contra {vilao.nome}!")
        sorte_mocinho = self.sorteio()
        sorte_vilao = vilao.sorteio()
        total_mocinho = sorte_mocinho + self.energia
        total_vilao = sorte_vilao + vilao.energia

        print(f"Sorte de {self.nome}: {sorte_mocinho}")
        print(f"Sorte de {vilao.nome}: {sorte_vilao}")

        if total_mocinho > total_vilao:
            print(f"{self.nome} venceu a luta!")
            self.incremento(2)
            vilao.decremento(2)
            self.registrar_batalha(f"Vitória contra {vilao.nome}")
            vilao.registrar_batalha(f"Derrota contra {self.nome}")
        elif total_mocinho < total_vilao:
            print(f"{vilao.nome} venceu a luta!")
            self.decremento(2)
            vilao.incremento(2)
            self.registrar_batalha(f"Derrota contra {vilao.nome}")
            vilao.registrar_batalha(f"Vitória contra {self.nome}")
        else:
            print("A luta terminou em empate!")
            self.decremento(1)
            vilao.decremento(1)
            self.registrar_batalha(f"Empate com {vilao.nome}")
            vilao.registrar_batalha(f"Empate com {self.nome}")

    def interagir(self, outro_personagem):
        print(f"{self.nome} conversou amigavelmente com {outro_personagem.nome}.")

class Vilao(Personagem):
    #alimentar vilão
    def alimentar(self):
        if self.energia <= 0:
            print(f"{self.nome} está morto e não pode ser alimentado.")
        else:
            self.incremento(3)
            print(f"{self.nome} foi alimentado e ganhou 3 pontos de energia.")
    def atacar(self, mocinho):
        dano = random.randint(1, 3)
        mocinho.decremento(dano)
        print(f"{self.nome} atacou {mocinho.nome}, causando {dano} de dano.")

    #caracteristica do vilão
    def zombar(self):
        print(f"{self.nome} está zombando dos mocinhos!")

    #luta do vilão
    def lutar(self, mocinho):
        print(f"{self.nome} está lutando contra {mocinho.nome}!")
        sorte_vilao = self.sorteio()
        sorte_mocinho = mocinho.sorteio()
        total_vilao = sorte_vilao + self.energia
        total_mocinho = sorte_mocinho + mocinho.energia

        print(f"Sorte de {self.nome}: {sorte_vilao}")
        print(f"Sorte de {mocinho.nome}: {sorte_mocinho}")

        if total_vilao > total_mocinho:
            print(f"{self.nome} venceu a luta!")
            self.incremento(2)
            mocinho.decremento(2)
            self.registrar_batalha(f"Vitória contra {mocinho.nome}")
            mocinho.registrar_batalha(f"Derrota contra {self.nome}")
        elif total_vilao < total_mocinho:
            print(f"{mocinho.nome} venceu a luta!")
            self.decremento(2)
            mocinho.incremento(2)
            self.registrar_batalha(f"Derrota contra {mocinho.nome}")
            mocinho.registrar_batalha(f"Vitória contra {self.nome}")
        else:
            print("A luta terminou em empate!")
            self.decremento(1)
            mocinho.decremento(1)
            self.registrar_batalha(f"Empate com {mocinho.nome}")
            mocinho.registrar_batalha(f"Empate com {self.nome}")

    def interagir(self, outro_personagem):
        print(f"{self.nome} desafiou {outro_personagem.nome} para uma batalha!")
