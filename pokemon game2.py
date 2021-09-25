class Pokemon:
  def __init__(self,name, health = 100, level = 1, type):
    self.name = name
    self.health = health
    self.type = type
    self.level = level
  
  def health_loss(self,health):
    self.health -= 0
      


class Trainer:
  def __init__(self, name):
    self.name = name


#this is test
test = 'new'

pokemon_1 = Pokemon("pikachu", "electric")
pokemon_2 = Pokemon("bulbasaur" "water")
pokemon_3 = Pokemon("charmendar" "fire")

trainer_1 = Trainer("ash")
trainer_2 = Trainer("misty")
trainer_3 = Trainer("team rocket")
