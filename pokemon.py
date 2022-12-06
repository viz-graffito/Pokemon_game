import discord
import random
TOKEN = ''
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def response(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if user_message.lower() == 'hi':
      await message.channel.send(f'Hey')
    return

client.run(TOKEN)


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
  
  def health_status(self):
    print(f'{self.name} current health is {self.health}')

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
    elif (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
      print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
      print("It's not very effective")
      other_pokemon.lose_health(round(self.level * 0.5))
        
    elif (self.type == other_pokemon.type):
      print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
      other_pokemon.lose_health(self.level)
        
    elif (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
      print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
      print("It's super effective")
      other_pokemon.lose_health(self.level * 2)
    elif (self.type == 'Electric' and other_pokemon.type == 'Grass'):
      print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
      print("It's super effective")
      other_pokemon.lose_health(self.level * 2)
    else:
      print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
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

pokemon_1 = Pokemon(name = "pikachu", type = "Electric", level =1)
pokemon_2 = Pokemon(name = "bulbasaur", type = "Grass")
pokemon_3 = Pokemon(name = "charmendar", type = "Fire",level = 3)
pokemon_4 = Pokemon(name = "squirtle", type =  "Water")



trainer_1 = input('Welcome to pokemon. Please enter player1 name : ')
trainer_2 = input("Hi, " + str(trainer_1) + "! Welcome! Let's find you an opponent. Enter a name for the second player. : ")

choice = input(f"Hi, {trainer_1}! Let's pick our Pokemon! {trainer_1}, would you like a Level 1 pikachu, or a Level 3 bulbasaur? {trainer_2} will get the other one. Type either 'pikachu' or 'bulbasaur'. "
  ""
)

while choice != 'pikachu' and choice != 'bulbasaur':
  choice = input("Whoops, it looks like you didn't choose 'pikachu' or 'bulbasaur'. Try selecting one again! ")

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

print('fight is about to start!!')

print(f'{trainer_1_pokemon[0]} used electric thunderbolt attack to {trainer_2_pokemon[0]}')

pokemon_1.attack(pokemon_2)
pokemon_2.attack(pokemon_1)

