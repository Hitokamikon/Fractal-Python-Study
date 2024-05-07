from random import *

class DLA3d:
  def __init__(self , half_size : int) -> None:
    self.seeds = [(0,0,0)]
    self.half_size = half_size
    self.increase_countdown = 50
    self.create_practicle()
    pass

  def create_practicle(self):
    ra = random() * 6
    if ra > 5:
      self.practicle = (randint(-self.half_size , self.half_size) , randint(-self.half_size , self.half_size) , -self.half_size)
    if ra > 4:
      self.practicle = (randint(-self.half_size , self.half_size) , randint(-self.half_size , self.half_size) , self.half_size)
    elif ra > 3:
      self.practicle = (randint(-self.half_size , self.half_size) , self.half_size , randint(-self.half_size , self.half_size))
    elif ra > 2:
      self.practicle = (randint(-self.half_size , self.half_size) , -self.half_size , randint(-self.half_size , self.half_size))
    elif ra > 1:
      self.practicle = (self.half_size , randint(-self.half_size , self.half_size) , randint(-self.half_size , self.half_size))
    else:
      self.practicle = (-self.half_size , randint(-self.half_size , self.half_size) , randint(-self.half_size , self.half_size))
    pass

  def run(self):
    ra = random() * 6
    if ra > 5:
      self.practicle = (self.practicle[0] + 1 , self.practicle[1] , self.practicle[2])
    elif ra > 4:
      self.practicle = (self.practicle[0] - 1 , self.practicle[1] , self.practicle[2])
    elif ra > 3:
      self.practicle = (self.practicle[0] , self.practicle[1] + 1 , self.practicle[2])
    elif ra > 2:
      self.practicle = (self.practicle[0] , self.practicle[1] - 1 , self.practicle[2])
    elif ra > 1:
      self.practicle = (self.practicle[0] , self.practicle[1] , self.practicle[2] + 1)
    else:
      self.practicle = (self.practicle[0] , self.practicle[1] , self.practicle[2] - 1)
    
    if abs(self.practicle[0]) > self.half_size or abs(self.practicle[1]) > self.half_size or abs(self.practicle[2]) > self.half_size:
      self.create_practicle()
    for seed in self.seeds:
      if(abs(seed[0] - self.practicle[0]) + abs(seed[1] - self.practicle[1]) + abs(seed[2] - self.practicle[2])) == 1:
        self.seeds.append(self.practicle)
        self.create_practicle()
        self.increase_countdown -= 1
        if self.increase_countdown <= 0:
          self.increase_countdown += 50
          self.half_size += 1

        break
    
    pass