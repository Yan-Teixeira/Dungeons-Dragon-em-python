#Aluno Yan dos Santos Teixeira M: 2023010530
import random
import time
from personagens import Personagem, Mocinho, Vilao

def menu():
    print("====== ミ༺𝘋𝘶𝘯𝘨𝘦𝘰𝘯𝘴 & 𝘋𝘳𝘢𝘨𝘰𝘯𝘴༻🐲彡 =======")
    print("‖                                       ‖ ")
    print("‖     1. Criar personagem               ‖ ")
    print("‖     2. Iniciar Duelo                  ‖ ")
    print("‖     3. Realizar torneios              ‖ ")
    print("‖     4. Alimentar                      ‖ ")
    print("‖     5. Interagir                      ‖ ")
    print("‖     6. Personagens criados            ‖ ")
    print("‖     7. Sair do jogo                   ‖ ")
    print("=========================================")

def criar_personagem():
    print("Selecione o tipo de personagem:")
    print("1. Mocinho")
    print("2. Vilão")
    tipo_opcao = input("Escolha uma opção: ")
    nome = input("Digite o nome do personagem: ")
    if tipo_opcao == "1":
        return Mocinho(nome)
    elif tipo_opcao == "2":
        return Vilao(nome)
    else:
        print("opção invalida.")
        return None

#historico
def mostrar_personagens(personagens):
    if not personagens:
        print("Nenhum personagem criado.")
    else:
        for personagem in personagens:
            print(personagem)

#duelo
def iniciar_duelo(personagens):
    mocinhos = [p for p in personagens if isinstance(p, Mocinho)]
    viloes = [p for p in personagens if isinstance(p, Vilao)]

    if not mocinhos or not viloes:
        print("É necessário pelo menos um mocinho e um vilão para iniciar o duelo.")
        return

    print("Mocinhos disponíveis:")
    for i, mocinho in enumerate(mocinhos):
        print(f"{i + 1}. {mocinho.nome}")

    print("Vilões disponíveis:")
    for i, vilao in enumerate(viloes):
        print(f"{i + 1}. {vilao.nome}")

    try:
        mocinho_index = int(input("Escolha um mocinho pelo número: ")) - 1
        vilao_index = int(input("Escolha um vilão pelo número: ")) - 1
        mocinho_escolhido = mocinhos[mocinho_index]
        vilao_escolhido = viloes[vilao_index]

        # Sorteio para duelo sem somar energia
        sorte_mocinho = mocinho_escolhido.sorteio()
        sorte_vilao = vilao_escolhido.sorteio()

        print(f"Sorte de {mocinho_escolhido.nome}: {sorte_mocinho}")
        print(f"Sorte de {vilao_escolhido.nome}: {sorte_vilao}")

        if sorte_mocinho > sorte_vilao:
            print(f"{mocinho_escolhido.nome} venceu o duelo!")
            mocinho_escolhido.incremento(2)
            vilao_escolhido.decremento(2)
            mocinho_escolhido.registrar_batalha(f"Vitória contra {vilao_escolhido.nome}")
            vilao_escolhido.registrar_batalha(f"Derrota contra {mocinho_escolhido.nome}")
        elif sorte_mocinho < sorte_vilao:
            print(f"{vilao_escolhido.nome} venceu o duelo!")
            vilao_escolhido.incremento(2)
            mocinho_escolhido.decremento(2)
            vilao_escolhido.registrar_batalha(f"Vitória contra {mocinho_escolhido.nome}")
            mocinho_escolhido.registrar_batalha(f"Derrota contra {vilao_escolhido.nome}")
        else:
            print("O duelo terminou em empate!")
            mocinho_escolhido.decremento(1)
            vilao_escolhido.decremento(1)
            mocinho_escolhido.registrar_batalha(f"Empate com {vilao_escolhido.nome}")
            vilao_escolhido.registrar_batalha(f"Empate com {mocinho_escolhido.nome}")
    except (ValueError, IndexError):
        print("Opção inválida. Por favor, escolha um número válido.")
    mocinhos = [p for p in personagens if isinstance(p, Mocinho)]
    viloes = [p for p in personagens if isinstance(p, Vilao)]

    if not mocinhos or not viloes:
        print("É necessário pelo menos um mocinho e um vilão para iniciar o duelo.")
        return

    print("Mocinhos disponíveis:")
    for i, mocinho in enumerate(mocinhos):
        print(f"{i + 1}. {mocinho.nome}")

    print("Vilões disponíveis:")
    for i, vilao in enumerate(viloes):
        print(f"{i + 1}. {vilao.nome}")

    try:
        mocinho_index = int(input("Escolha um mocinho pelo número: ")) - 1
        vilao_index = int(input("Escolha um vilão pelo número: ")) - 1
        mocinho_escolhido = mocinhos[mocinho_index]
        vilao_escolhido = viloes[vilao_index]
        mocinho_escolhido.lutar(vilao_escolhido)
    except (ValueError, IndexError):
        print("Opção inválida. Por favor, escolha um número válido.")

#torneio
def realizar_torneio(personagens):
    print("Iniciando torneio entre todos os personagens!")

    if len(personagens) < 2:
        print("É necessário pelo menos dois personagens para realizar um torneio.")
        return

    # Todos lutam contra todos
    for i in range(len(personagens)):
        for j in range(i + 1, len(personagens)):
            p1 = personagens[i]
            p2 = personagens[j]
            print(f"Duelo entre {p1.nome} e {p2.nome}!")
            p1.lutar(p2)

    # Determinar o vencedor com maior energia
    vencedor = max(personagens, key=lambda p: p.energia)

    print(f"O vencedor do torneio é {vencedor.nome} com {vencedor.energia} de energia!")
    print("Histórico do vencedor:")
    for batalha in vencedor.historico_batalhas:
        print(f"- {batalha}")
    print("Iniciando torneio entre múltiplos personagens!")

    if len(personagens) < 2:
        print("É necessário pelo menos dois personagens para realizar um torneio.")
        return

    participantes = personagens[:]

    while len(participantes) > 1:
        p1, p2 = random.sample(participantes, 2)
        print(f"Duelo entre {p1.nome} e {p2.nome}!")
        p1.lutar(p2)

        if p1.energia <= 0:
            participantes.remove(p1)
        if p2.energia <= 0:
            participantes.remove(p2)

    vencedor = participantes[0]
    print(f"O vencedor do torneio é {vencedor.nome} com {vencedor.energia} de energia!")
    print("Histórico do vencedor:")
    for batalha in vencedor.historico_batalhas:
        print(f"- {batalha}")
    print("Iniciando torneio entre mocinhos e vilões!")

    mocinhos = [p for p in personagens if isinstance(p, Mocinho)]
    viloes = [p for p in personagens if isinstance(p, Vilao)]

    if not mocinhos or not viloes:
        print("É necessário pelo menos um mocinho e um vilão para realizar o torneio.")
        return

    while len(mocinhos) > 1 or len(viloes) > 1:
        if len(mocinhos) > 1:
            p1, p2 = random.sample(mocinhos, 2)
            print(f"Duelo entre mocinhos: {p1.nome} vs {p2.nome}")
            p1.lutar(p2)
            if p1.energia <= 0:
                mocinhos.remove(p1)
            if p2.energia <= 0:
                mocinhos.remove(p2)

        if len(viloes) > 1:
            p1, p2 = random.sample(viloes, 2)
            print(f"Duelo entre vilões: {p1.nome} vs {p2.nome}")
            p1.lutar(p2)
            if p1.energia <= 0:
                viloes.remove(p1)
            if p2.energia <= 0:
                viloes.remove(p2)

    if mocinhos and viloes:
        print(f"Duelo final: {mocinhos[0].nome} vs {viloes[0].nome}")
        mocinhos[0].lutar(viloes[0])

        vencedor = mocinhos[0] if mocinhos[0].energia > 0 else viloes[0]
        print(f"O vencedor do torneio é {vencedor.nome} com {vencedor.energia} de energia!")
        print("Histórico de batalhas do vencedor:")
        for batalha in vencedor.historico_batalhas:
            print(f"- {batalha}")
    else:
        print("Não houve vencedor no torneio devido à falta de competidores.")
#interagir
def interagir_personagens(personagens):
    if len(personagens) < 2:
        print("É necessário pelo menos dois personagens para interagir.")
        return

    print("Personagens disponíveis:")
    for i, personagem in enumerate(personagens):
        print(f"{i + 1}. {personagem.nome}")

    try:
        p1_index = int(input("Escolha o primeiro personagem pelo número: ")) - 1
        p2_index = int(input("Escolha o segundo personagem pelo número: ")) - 1

        if p1_index < 0 or p1_index >= len(personagens) or p2_index < 0 or p2_index >= len(personagens):
            raise IndexError

        p1 = personagens[p1_index]
        p2 = personagens[p2_index]

        if p1.energia <= 0:
            print(f"{p1.nome} está morto e não pode interagir.")
            return
        if p2.energia <= 0:
            print(f"{p2.nome} está morto e não pode ser alvo de interação.")
            return

        print("Selecione a interação:")
        print("1. Conversar")
        print("2. Desafiar")
        acao = input("Escolha uma ação: ")

        if acao == "1":
            if isinstance(p1, Mocinho):
                print(f"{p1.nome} conversou com {p2.nome}. {p2.nome} ganhou 1 ponto de energia.")
                p2.incremento(1)
            elif isinstance(p1, Vilao):
                print(f"{p1.nome} zombou de {p2.nome}. {p2.nome} perdeu 1 ponto de energia.")
                p2.decremento(1)
            else:
                print("Interação inválida.")
        elif acao == "2":
            print(f"{p1.nome} desafiou {p2.nome} para um duelo!")
            p1.lutar(p2)
        else:
            print("Ação inválida.")
    except (ValueError, IndexError): ##index valida o índice fornecido pelo usuário
        print("Opção inválida. Por favor, escolha um número válido.")
    if len(personagens) < 2:
        print("É necessário pelo menos dois personagens para interagir.")
        return

    print("Personagens disponíveis:")
    for i, personagem in enumerate(personagens):
        print(f"{i + 1}. {personagem.nome}")

    try:
        p1_index = int(input("Escolha o primeiro personagem pelo número: ")) - 1
        p2_index = int(input("Escolha o segundo personagem pelo número: ")) - 1

        if p1_index < 0 or p1_index >= len(personagens) or p2_index < 0 or p2_index >= len(personagens):
            raise IndexError

        p1 = personagens[p1_index] 
        p2 = personagens[p2_index]

        if p1.energia <= 0:
            print(f"{p1.nome} está morto e não pode interagir.\n")
            return
        if p2.energia <= 0:
            print(f"{p2.nome} está morto e não pode ser alvo de interação.\n")
            return

        if isinstance(p1, Mocinho):
            print(f"{p1.nome} conversou com {p2.nome}. {p2.nome} ganhou 1 ponto de energia.")
            p2.incremento(1)
        elif isinstance(p1, Vilao):
            print(f"{p1.nome} zombou de {p2.nome}. {p2.nome} perdeu 1 ponto de energia.")
            p2.decremento(1)
        else:
            print("Interação inválida.")
    except (ValueError, IndexError):
        print("Opção inválida. Por favor, escolha um número válido.")

#alimentando personagem e não alimentando aqueles personagens que estão mortos
def alimentar_personagem(personagens):
    if not personagens:
        print("Nenhum personagem criado para alimentar.")
        return

    print("Personagens disponíveis para alimentação:")
    for i, personagem in enumerate(personagens):
        print(f"{i + 1}. {personagem.nome}")

    try:
        escolha = int(input("Escolha o número do personagem para alimentar: ")) - 1
        if escolha < 0 or escolha >= len(personagens):
            raise IndexError
        personagem = personagens[escolha]
        if personagem.energia <= 0:
            print(f"{personagem.nome} está morto e não pode ser alimentado.") #personagens que morreram e não podem ser alimentados 
        else:
            personagem.alimentar()
    except (ValueError, IndexError): 
        print("Opção inválida. Por favor, escolha um número válido.")
    if not personagens:
        print("Nenhum personagem criado para alimentar.")
        return

    print("Personagens disponíveis para alimentação:")
    for i, personagem in enumerate(personagens):
        print(f"{i + 1}. {personagem.nome}")

    try:
        escolha = int(input("Escolha o número do personagem para alimentar: ")) - 1
        if escolha < 0 or escolha >= len(personagens):
            raise IndexError
        personagem = personagens[escolha]
        personagem.alimentar()
    except (ValueError, IndexError):
        print("Opção inválida. Por favor, escolha um número válido.")


def sair_do_jogo():
    print("saindo do jogo...")
    time.sleep(2)
    exit()

def main():
    personagens = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            personagem = criar_personagem()
            if personagem:
                personagens.append(personagem)
            time.sleep(3)  
        elif opcao == "2":
            iniciar_duelo(personagens)
            time.sleep(3) 
        elif opcao == "3":
            realizar_torneio(personagens)
            time.sleep(3)
        elif opcao == "4":
            alimentar_personagem(personagens)
        elif opcao == "5":
            interagir_personagens(personagens)
            time.sleep(3)
        elif opcao == "6":
            mostrar_personagens(personagens)
            time.sleep(3)  
        elif opcao == "7":
            sair_do_jogo()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(3)  

if __name__ == "__main__":
    main()
