O objetivo é criar uma aplicação interativa e funcional que simule a experiência do tradicional jogo de
bingo, com a capacidade de gerar cartelas aleatórias, sortear números e identificar os ganhadores.

jogo de Bingo, os participantes recebem cartelas com 25 números distintos dispostos em uma
matriz com 5 linhas e 5 colunas. Os números da primeira coluna devem estar no intervalo de 1 a 10,
da segunda, de 11 a 20, da terceira, de 21 a 30, da quarta, de 31 a 40 e da quinta, de 41 a 50.
+----------------+
| 10 14 23 39 42 |
| 07 13 21 37 44 |
| 04 20 22 31 43 |
| 08 11 28 40 41 |
| 05 17 30 34 49 |
+----------------+
Durante o jogo, números são sorteados e ao verificar que um número sorteado está em sua cartela, o
jogador deve marcá-lo. Ganha prêmios quem completar com números sorteados uma linha, uma
coluna ou uma das diagonais. Veja alguns exemplos abaixo:
+----------------++----------------++----------------++----------------+
| 10 14 23 39 42 || 10 XX 23 39 42 || XX 14 23 39 42 || 10 14 23 39 XX |
| 07 13 21 37 44 || 07 XX 21 37 44 || 07 XX 21 37 44 || 07 13 21 XX 44 |
| 04 20 22 31 43 || 04 XX 22 31 43 || 04 20 XX 31 43 || 04 20 XX 31 43 |
| XX XX XX XX XX || 08 XX 28 40 41 || 08 11 28 XX 41 || 08 XX 28 40 41 |
| 05 17 30 34 49 || 05 XX 30 34 49 || 05 17 30 34 XX || XX 17 30 34 49 |
+----------------++----------------++----------------++----------------+
