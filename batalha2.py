import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Pokemon: 
    def __init__(self, nome, tipo, vida, ataque, evolucao=None):
        self.nome = nome
        self.tipo = tipo
        self.vida_max = vida      # Mantém o registro do HP cheio para a cura
        self.vida = vida
        self.ataque = ataque
        self.evolucao = evolucao  # Nome da próxima forma (Ex: Raichu)
        self.nivel = 1
        self.exp = 0

    def atacar(self, outro_pokemon):
        # 1. Regra de Vantagem entre tipos
        vantagens = {
            "aquático": "fogo",
            "fogo": "elétrico",
            "elétrico": "aquático"
        }
        
        multiplicador = 1.0
        msg_vantagem = ""
        
        if vantagens.get(self.tipo) == outro_pokemon.tipo:
            multiplicador = 2.0
            msg_vantagem = "💥 Foi super efetivo!"
        elif vantagens.get(outro_pokemon.tipo) == self.tipo:
            multiplicador = 0.5
            msg_vantagem = "🛡️ Não foi muito efetivo..."

        # 2. Sistema de Ataques Críticos (15% de chance de causar 1.5x de dano)
        critico = 1.0
        msg_critico = ""
        if random.random() < 0.15:
            critico = 1.5
            msg_critico = "⭐ GOLPE CRÍTICO!"

        # Cálculo do dano final
        dano_final = int(self.ataque * multiplicador * critico)
        outro_pokemon.vida -= dano_final

        if outro_pokemon.vida < 0:
            outro_pokemon.vida = 0
            
        # Mensagens do combate
        print(f"⚔️ {self.nome} atacou {outro_pokemon.nome} e causou {dano_final} de dano!")
        if msg_vantagem: print(msg_vantagem)
        if msg_critico: print(msg_critico)

    # 3. Sistema de Cura
    def curar(self):
        quantidade_cura = int(self.vida_max * 0.5) # Cura 50% do HP máximo
        self.vida = min(self.vida_max, self.vida + quantidade_cura)
        print(f"🧪 {self.nome} usou uma Poção e recuperou {quantidade_cura} de vida!")

    # 5. Sistema de Evolução de Pokémon
    def ganhar_exp(self):
        self.exp += 50
        print(f"✨ {self.nome} ganhou 50 de EXP!")
        if self.exp >= 100:
            self.nivel += 1
            self.exp = 0
            # Aumenta os status em 20% ao subir de nível
            self.vida_max = int(self.vida_max * 1.2)
            self.vida = self.vida_max
            self.ataque = int(self.ataque * 1.2)
            print(f"⬆️ {self.nome} subiu para o Nível {self.nivel}! Seus status aumentaram!")
            
            # Se tiver uma evolução programada, ele evolui
            if self.evolucao:
                print(f"🌟 O que?! {self.nome} está evoluindo...")
                print(f"🎉 Parabéns! Seu {self.nome} evoluiu para {self.evolucao}!")
                self.nome = self.evolucao
                self.evolucao = None # Não evolui mais de uma vez

# Criando os Pokémons com seus respectivos nomes de evolução
Pokemon1 = Pokemon("Pikachu", "elétrico", 100, 25, evolucao="Raichu")
Pokemon2 = Pokemon("Charmander", "fogo", 110, 20, evolucao="Charmeleon")
Pokemon3 = Pokemon("Squirtle", "aquático", 120, 18, evolucao="Blastoise")
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

# Limitação de poções do jogador na partida
pocoes_disponiveis = 2

while pokemon_escolhido.vida > 0 and pokemon_adversario.vida > 0:
  print("\n1 - Atacar")
  print(f"2 - Usar Cura ({pocoes_disponiveis} restantes)")
  print("3 - Ver status")
  print("4 - Fugir")
  acao = input("Escolha uma ação: ")
  print()

  if acao == "1":
    pokemon_escolhido.atacar(pokemon_adversario)
    print(f"{pokemon_adversario.nome} ficou com {pokemon_adversario.vida} de vida.")

    if pokemon_adversario.vida > 0:
      print(f"\nTurno do adversário:")
      pokemon_adversario.atacar(pokemon_escolhido)
      print(f"Seu {pokemon_escolhido.nome} ficou com {pokemon_escolhido.vida} de vida.")

  elif acao == "2":
    if pocoes_disponiveis > 0:
      pokemon_escolhido.curar()
      pocoes_disponiveis -= 1
      
      # Turno do adversário após você se curar
      print(f"\nTurno do adversário:")
      pokemon_adversario.atacar(pokemon_escolhido)
      print(f"Seu {pokemon_escolhido.nome} ficou com {pokemon_escolhido.vida} de vida.")
    else:
      print("❌ Você não tem mais poções de cura!")

  elif acao == "3":
    print(f"{pokemon_escolhido.nome} (LV {pokemon_escolhido.nivel}): {pokemon_escolhido.vida}/{pokemon_escolhido.vida_max} de vida e {pokemon_escolhido.ataque} de ataque!")
    print(f"{pokemon_adversario.nome}: {pokemon_adversario.vida}/{pokemon_adversario.vida_max} de vida e {pokemon_adversario.ataque} de ataque!")
  elif acao == "4":
    print("_______________________________________")
    print()
    print("Você fugiu da batalha!")
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
  print("Você venceu a batalha! Parabéns, você é um mestre Pokémon!")
  print("__________________________________________________________")
  print()
  # Executa o ganho de EXP e possível evolução ao fim da vitória
  pokemon_escolhido.ganhar_exp()

