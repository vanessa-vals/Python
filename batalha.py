import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Pokemon : 
    def __init__(self, nome, tipo, vida, ataque):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque

    def atacar(self, outro_pokemon):
        outro_pokemon.vida -= self.ataque
        if outro_pokemon.vida < 0:
            outro_pokemon.vida = 0

Pokemon1 = Pokemon("Pikachu", "elétrico", 100, 25)
Pokemon2 = Pokemon("Charmander", "fogo", 110, 20)
Pokemon3 = Pokemon("Squirtle", "aquático", 120, 18)
pokemons = [Pokemon1, Pokemon2, Pokemon3]

print("_______________________________________")
print()
print(" Bem-vindo ao jogo de batalha Pokémon!")
print("_______________________________________")
print()
print("Escolha seu Pokémon:")
print("1 - Pikachu")
print("2 - Charmander")
print("3 - Squirtle")

opcao = int(input("Digite o número do Pokémon que deseja escolher: "))

if opcao == 1:
  pokemon_escolhido = Pokemon1
elif opcao == 2:
  pokemon_escolhido = Pokemon2
elif opcao == 3:
  pokemon_escolhido = Pokemon3
else:
  print("Opção inválida.")
  exit()

opcoes_adversario = [pokemon for pokemon in pokemons if pokemon != pokemon_escolhido]
pokemon_adversario = random.choice(opcoes_adversario)

print()
print(" Vamos a batalha Pokémon!")
print("_______________________________________")
print()
print(f"Você escolheu {pokemon_escolhido.nome}. Ele tem {pokemon_escolhido.vida} de vida e {pokemon_escolhido.ataque} de ataque!")
print(f"O seu adversário será: {pokemon_adversario.nome}. Ele tem {pokemon_adversario.vida} de vida e {pokemon_adversario.ataque} de ataque!")


while pokemon_escolhido.vida > 0 and pokemon_adversario.vida > 0:
  print("\n1 - Atacar")
  print("2 - Ver status")
  print("3 - Fugir")
  acao = input("Escolha uma ação: ")
  print()

  if acao == "1":
    pokemon_escolhido.atacar(pokemon_adversario)
    print(f"Que batalha impressionante!💥{pokemon_adversario.nome} ficou com {pokemon_adversario.vida} de vida.")

    if pokemon_adversario.vida > 0:
      pokemon_adversario.atacar(pokemon_escolhido)
  elif acao == "2":
    print(f"{pokemon_escolhido.nome}: {pokemon_escolhido.vida} de vida e {pokemon_escolhido.ataque} de ataque!")
    print(f"{pokemon_adversario.nome}: {pokemon_adversario.vida} de vida e {pokemon_adversario.ataque} de ataque!")
  elif acao == "3":
    print("_______________________________________")
    print()
    print("Você fugiu da batalha!❌ ")
    print("_______________________________________")
    break
  else:
    print("Opção inválida.")
if pokemon_escolhido.vida <= 0:
  print()
  print("Seu Pokémon foi derrotado.")
elif pokemon_adversario.vida <= 0:
  print()
  print("_________________________________________________________")
  print()
  print("Você venceu a batalha!⭐ Parabéns, você é um mestre Pokémon!")
  print("__________________________________________________________")
  print()





   




  
  






