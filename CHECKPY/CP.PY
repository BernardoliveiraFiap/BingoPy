import random
import os
#RM551356 ENZO OLIVEIRA
#RM551416 MACIRANDER
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartela = self.gerar_cartela()

    def gerar_cartela(self):
        cartela = []
        for i in range(5):
            coluna = random.sample(range(1 + i*10, 11 + i*10), 5)
            cartela.append(coluna)
        return cartela

    def marcar_numero(self, num):
        for i in range(5):
            for j in range(5):
                if self.cartela[i][j] == num:
                    self.cartela[i][j] = 'XX'
                    return

    def verificar_vencedor(self):
        # Verificar linhas
        for linha in zip(*self.cartela):
            if all(num == 'XX' for num in linha):
                return True
        # Verificar colunas
        for coluna in self.cartela:
            if all(num == 'XX' for num in coluna):
                return True
        # Verificar diagonais
        if all(self.cartela[i][i] == 'XX' for i in range(5)):
            return True
        if all(self.cartela[i][4-i] == 'XX' for i in range(5)):
            return True
        return False

def imprimir_cartela(cartela):
    for linha in zip(*cartela):
        print(' '.join(str(num).rjust(2) for num in linha))

def jogar_bingo(jogadores):
    numeros_sorteados = []
    
    while True:
        input("Pressione Enter para sortear um número.")
        num = random.randint(1, 50)
        while num in numeros_sorteados:
            num = random.randint(1, 50)
        
        numeros_sorteados.append(num)
        print(f"\nNúmero sorteado: {num}")
        
        for jogador in jogadores:
            jogador.marcar_numero(num)
            print(f"\nCartela do {jogador.nome}:")
            imprimir_cartela(jogador.cartela)
            
            if jogador.verificar_vencedor():
                print(f"\nParabéns, {jogador.nome} ganhou!")
                return jogador.nome

def atualizar_ranking(vencedor):
    ranking = {}
    if os.path.exists('ranking.txt'):
        with open('ranking.txt', 'r') as f:
            for linha in f:
                nome, vitorias = linha.strip().split()
                ranking[nome] = int(vitorias)

    if vencedor in ranking:
        ranking[vencedor] += 1
    else:
        ranking[vencedor] = 1

    with open('ranking.txt', 'w') as f:
        for nome, vitorias in ranking.items():
            f.write(f"{nome} {vitorias}\n")

def exibir_ranking():
    print("\nRanking de jogadores:")
    if os.path.exists('ranking.txt'):
        with open('ranking.txt', 'r') as f:
            for linha in f:
                print(linha.strip())

def main():
    num_jogadores = int(input("Digite a quantidade de jogadores (de 1 a 4): "))
    jogadores = [Jogador(input(f"Digite o nome do jogador {i+1}: ")) for i in range(num_jogadores)]
    
    vencedor = jogar_bingo(jogadores)
    print(f"\nO vencedor é {vencedor}!")
    
    atualizar_ranking(vencedor)
    
    exibir_ranking()

if __name__ == "__main__":
    main()