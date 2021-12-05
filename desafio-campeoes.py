# Qual o objetivo do código ?  Trazer como jogo o livro Desafio dos Campeões.
import time
import sys
import random
from random import randint

# Funções primárias para estética do game

# Simples função para exibir letras no estilo "Typewriting"


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00000001)

# Função de rolagem de dados de 6 faces


def dados(quantidade=1):
    return randint(quantidade, 6*quantidade)


def habilidade():
    return dados() + 6


def energia():
    return dados(2) + 12


def sorte():
    return dados() + 6


def criar_jogador(nome_jogador = 'Sem nome'):
    return {
        'Nome': nome_jogador,
        'Habilidade': habilidade(),
        'Energia': energia(),
        'Sorte' : sorte()
    }

sartorio = criar_jogador('Sartorio')

print(sartorio)

def perder_sorte(jogador, pontos_perdidos):
    jogador ['Sorte'] -= pontos_perdidos

perder_sorte(sartorio, 2)

print(sartorio)

def aranha_pica_ok(jogador):
    perder_sorte(jogador, 2)

for x in range(10):
    print(criar_jogador())

# Funcionamento do game

# Existem 3 valores a serem definidos por rolagem, os pontos de HABILIDADE, ENERGIA e SORTE,
# que mudam constantemente durante uma aventura, por isso a importância de serem dados mutáveis.
# Estes valores serão definidos de acordo com a função dados(), que recebe valores aleatórios
# de uma rolagem do dado de 6 faces.

# habilidade
# energia
# sorte

