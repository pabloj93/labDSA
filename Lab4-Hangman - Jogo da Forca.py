# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

#função para limpar a tela a cada execução

def limpa_tela():
    #windows
    if name == 'nt':
        _ = system('cls')
     #mac ou linux
    else:
        _ = system('clear')
       

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman():
	# Método Construtor
     def __init__(self, palavra): 
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_escolhidas = []

	# Método para adivinhar a letra
     def guess(self, letra):
          if letra in self.palavra and letra not in self.letras_escolhidas:
               self.letras_escolhidas.append(letra)
          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else:
               return False
          
          return True
     
	# Método para verificar se o jogo terminou
     def hangman_over(self, pontos):
          return self.hangman_won(pontos) or (len(self.letras_erradas) == 6)
     
	# Método para verificar se o jogador venceu
     def hangman_correct(self):

          if '_' not in self.hide_palavra():	
               return True
          return False
     
     def hangman_won(self, pontos):
          if pontos == 50:
               return True
          return False
	# Método para não mostrar a letra no board
     def hide_palavra(self):

          rtn = ''

          for letra in self.palavra:
               if letra not in self.letras_escolhidas:
                    rtn  += '_'
               else:
                    rtn += letra
          return rtn
          
	# Método para checar o status do game e imprimir o board na tela
     def print_game_status(self):
          print(board[len(self.letras_erradas)])

          print('\nPalavra: ' + self.hide_palavra())

          print('\nLetras erradas: ',)
          for letra in self.letras_erradas:
               print(letra,)

          print()

          print('Letras corretas: ',)
          for letra in self.letras_escolhidas:
               print(letra,)
          
          print()
     
def rand_palavra(escolha):
     animais = [
    'cachorro', 'gato', 'elefante', 'leao', 'tigre', 'girafa', 'hipopotamo', 'rinoceronte', 'zebra', 'macaco',
    'coelho', 'rato', 'esquilo', 'guaxinim', 'panda', 'urso', 'papagaio', 'periquito', 'coruja', 'pombo',
    'aguia', 'falcao', 'pato', 'cisne', 'flamingo', 'avestruz', 'galinha', 'galo', 'pintinho', 'pavao',
    'tartaruga', 'cobra', 'jacare', 'crocodilo', 'lagarto', 'lagartixa', 'sapo', 'ra', 'salamandra', 'tritao',
    'peixe', 'tubarao', 'baleia', 'golfinho']
     
     nomes = [
    'João', 'Maria', 'Pedro', 'Ana', 'José', 'Carla', 'Luiz', 'Fernanda', 'Paulo', 'Mariana',
    'Carlos', 'Beatriz', 'Ricardo', 'Aline', 'Gabriel', 'Patrícia', 'Lucas', 'Vanessa', 'Gustavo', 'Camila',
    'Miguel', 'Larissa', 'Rafael', 'Jéssica', 'Mateus', 'Amanda', 'Diego', 'Isabela', 'Felipe', 'Juliana',
    'Daniel', 'Laura', 'Thiago', 'Letícia', 'Vinícius', 'Natália', 'Eduardo', 'Tatiana', 'Alexandre', 'Adriana',
    'Caio', 'Priscila', 'Leonardo', 'Cristina', 'Fábio', 'Renata', 'Bruno', 'Mônica', 'Rodrigo', 'Bianca',
    'Guilherme', 'Sandra', 'Marcelo', 'Renan', 'André', 'Elaine', 'Fernando', 'Raquel', 'Vitor', 'Evelyn',
    'Henrique', 'Carolina', 'Jorge', 'Heloísa', 'Raul', 'Talita', 'Sérgio', 'Natalia', 'William', 'Valentina',
    'Adriano', 'Rebeca', 'Hugo', 'Yasmin', 'Erick', 'Daniela', 'Roberto', 'Sabrina', 'Douglas', 'Lorena',
    'Murilo', 'Cintia', 'Alan', 'Esther', 'Marcela', 'Júlio', 'Luana', 'Otávio', 'Isadora', 'Caíque', 'Débora',
    'Igor', 'Júlia', 'Silvio', 'Sônia', 'Ronaldo', 'Teresa', 'Wagner', 'Vivian', 'Álvaro', 'Verônica']
     
     frutas = [
    'abacaxi', 'acerola', 'amora', 'banana', 'caju', 'cereja', 'coco', 'figo', 'framboesa', 'goiaba',
    'laranja', 'limao', 'maca', 'mamao', 'manga', 'maracuja', 'melancia', 'melao', 'morango', 'nectarina',
    'pera', 'pessego', 'pitanga', 'pitaya', 'romã', 'uva', 'abacate', 'ameixa', 'ameixa-seca', 'kiwi',
    'tangerina', 'jabuticaba', 'jaboticaba', 'jaca', 'caqui', 'cajá', 'graviola', 'lichia', 'noni', 'tamarindo',
    'sapoti', 'acerola', 'jambo', 'atemoia', 'caimito', 'calamondin', 'cupuaçu', 'pêssego', 'sapoti', 'sapucaia',
    'jenipapo', 'umbu', 'tucumã', 'tucuma', 'toranja', 'laranja-lima', 'laranja-pera', 'cajuí', 'cupuaçu', 'cupuassu',
    'tucumã-do-pará', 'tucuma-do-para', 'murici', 'buriti', 'castanha-do-brasil', 'castanha-do-para', 'castanha-de-caju', 'castanha-de-baru', 'jujuba', 'cambuci',
    'camu-camu', 'fruta-do-conde', 'grumixama', 'murta', 'fruta-do-lobo', 'pequi', 'cagaita', 'guabiroba', 'guarana', 'ingá',
    'marmelo', 'piqui', 'sapoti', 'araca', 'araticum', 'biribá', 'curuba', 'guabiju', 'grumixama', 'ingá',
    'jenipapo', 'pequi', 'pupunha', 'tucumã', 'uváia']
     
     if escolha == "1":
          palavra = random.choice(animais)
     elif escolha == "2":
          palavra = random.choice(nomes)
     else: 
          palavra = random.choice(frutas)
     return palavra

#metodo main - execução do programa
def main():
     limpa_tela()
     print("Bem Vindo ao jogo da Forca!")
     print("\nSelecione grupo de palavras para jogar:\n1-Animais\n2-Nomes Próprios\n3-Fru1tas")
     escolha = input('\nQual sua escolha (1, 2 ou 3):')

     #cria o objeto e seleciona uma palavra randomicamente
     game = Hangman(rand_palavra(escolha))
     pontos = 0
     #enquanto o jogo não terminar, print do status, solicita umna letra e faz a leitura do caracter
     while not game.hangman_over(pontos):

          #status do game
          game.print_game_status()

          #recebe letra do jogador
          user_input = input('\nDigite uma Letra: ')

          #verifica se a letra digitada faz parte da palavra
          game.guess(user_input)

          if game.hangman_correct():
               pontos += 1
               limpa_tela()
               print('\nA palavra era '+ game.palavra)
               print('\nSeu total de pontos é '+ str(pontos))
               game = Hangman(rand_palavra(escolha))
          else:
               pass


     #verifica o status do jogo
     game.print_game_status()

     #de acordo com o status, imprime mensagem na tela para o usuário
     if game.hangman_won(pontos):
          print('\nParabéns! Você venceu!! Com um total de 50 pontos!')
     else:
          print('\nGame Over! Você Perdeu.')
          print('\nA palavra era '+ game.palavra)
          print('\nSeu total de pontos foi '+ str(pontos))

#executa o programa
if __name__ == "__main__":
     main()




