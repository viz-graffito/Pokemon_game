# import discord
TOKEN = ''
# client = discord.Client()

# @client.event
# async def on_ready():
  # print('We have logged in as {0.user}'.format(client))

# client.runt(TOKEN)

class Pokemon:
  def __init__(self, name, type, level = 5):
    self.name = name
    self.health = level * 5
    self.type = type
    self.level = level
    self.max_health = level * 5
    self.is_knocked_out = False
  
  def __repr__(self):
    return 'your {name} is on {level} and it\'s current health is {health}, {name} is {type} type pokemon.'.format(name = self.name, level = self.level, health = self.health, type = self.type)
  
  def lose_health(self,health):
    self.health -= 0

  def regaining_health(self,health):
    self.health += 1
  
  def knock_out(self):
    self.is_knocked_out = True
    if self.health != 0:
      self.health = 0
    print('{name} is knocked out!'.format(name = self.name))

  def lose_health(self, ammount):
    self.health -= ammount
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    else:
     print('{name} now has {health} health.'.format(name = self.name, health = self.health))

  def gain_health(self, ammount):
    self.health += ammount
    if self.health >= self.max_health:
      self.health = self.max_health
    print('{name} now has {health} health.'.format(name = self.name, health = self.health))
  
  def attack(self,other_pokemon):
    if self.is_knocked_out:
      print('{name} can\'t attack because it is knocked out!'.format(name=self.name))
      # return
    if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
            print("It's not very effective")
            other_pokemon.lose_health(round(self.level * 0.5))
        
    if (self.type == other_pokemon.type):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
            other_pokemon.lose_health(self.level)
        
    if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)

class Trainer:
  def __init__(self, name, pokemon_list):
    self.name = name
    self.pokemons = pokemon_list
    self.current_pokemon = 0
  
  def __repr__(self):
    print('The trainer {name} has the following pokemon.'.format(name = self.name))
    for pokemon in self.pokemons:
      print(pokemon)
    return "the current active pokemon is {name}.".format(name = self.pokemons[self.current_pokemon].name)

  def attack_other_trainer(self, other_trainer):
    my_pokemon = self.pokemon[self.current_pokemon]
    their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
    my_pokemon.attack(their_pokemon)

pokemon_1 = Pokemon(name = "pikachu", type = "electric", level =7)
pokemon_2 = Pokemon(name = "bulbasaur", type = "grass")
pokemon_3 = Pokemon(name = "charmendar", type = "fire",level = 9)
pokemon_4 = Pokemon(name = "squirtle", type =  "water")



trainer_1 = input('Welcome to pokemon. Please enter player1 name')
trainer_2 = input("Hi, " + str(trainer_1) + "! Welcome! Let's find you an opponent. Enter a name for the second player. ")

choice = input("Hi, " + trainer_2 + "! Let's pick our Pokemon! " + trainer_1 + ", would you like a Level 7 pikachu, or a Level 7 bulbasaur? " + trainer_2 + " will get the other one. Type either 'pikachu' or 'bulbasaur'. ")

while choice != 'pikachu' and choice != 'squirtle':
  choice = input("Whoops, it looks like you didn't choose 'pikachu' or 'Squirtle'. Try selecting one again! ")

trainer_1_pokemon = []
trainer_2_pokemon = []

if choice == 'pikachu':
  trainer_1_pokemon.append(pokemon_1)
  trainer_2_pokemon.append(pokemon_2)

else:
  trainer_1_pokemon.append(pokemon_2)
  trainer_2_pokemon.append(pokemon_1)

trainer_one = Trainer(trainer_1, trainer_1_pokemon)
trainer_two = Trainer(trainer_2, trainer_2_pokemon)

print('lets get ready to fight! here are out two trainers')

print(trainer_one)
print(trainer_two)