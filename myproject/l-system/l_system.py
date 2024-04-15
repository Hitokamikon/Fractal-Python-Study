import numpy as np
import string
import array as array
import random

class production:
    """
    产生式
    """

    def __init__(self , predecessor , successor , * , p = 1) :
        """
        构造函数

        Parameters
        ----------
        predecessor : 前驱
        successor : 后继
        p : 概率
        """
        self.predecessor = predecessor
        self.successor =successor
        self.p = p

class l_system:
    """
    L-系统
    """
    def __init__(self , ps : array):
        self.ps = ps

    def produce(self , v:string):
        result = ""
        for char in v:
            findP = False
            ra = random.random()
            for p in self.ps:
                if findP :
                    break
                if p.predecessor == char:
                    if ra <= p.p:
                      result += p.successor
                      findP = True
                    ra -= p.p
            if not findP:
                result += char
               
        return result

class stack:
  def __init__ (self) -> None:
    self.stack=[]

  def isEmpty(self):
    return self.stack==[]
  
  def push(self,item):
    self.stack.append(item)
  
  def pop(self):
    if self.isEmpty():
      raise IndexError
    return self.stack.pop()
  
  def peek(self):
    return self.stack[-1]
  
  def size(self):
    return len(self.stack)

class turtle:
    """
    海龟
    """
    def __init__(self , d , alpha , * , s = 1) -> None:
        self.d = d
        self.alpha = alpha
        self.s = s

    def run(self , word : string) :
        heading = 0
        length = self.d
        points = [(0,0)]
        x = 0
        y = 0
        curves = []
        state_stack = stack()
        for letter in word:
            if letter == "f" or letter == "g" or letter == "e" or letter == "L" or letter == "R":
                x += length * np.cos(heading)
                y += length * np.sin(heading)
                length = length * self.s
                points.append((x,y))
            elif letter == "+":
                heading += self.alpha
            elif letter == "-":
                heading -= self.alpha
            elif letter == "h":
                curves.append(points)
                x += length * np.cos(heading)
                y += length * np.sin(heading)
                points = [(x,y)]
            elif letter == "[":
                state_stack.push((x,y,heading,length))
            elif letter == "]":
                state = state_stack.pop()
                x = state[0]
                y = state[1]
                heading = state[2]
                length = state[3]
                curves.append(points)
                points = [(x,y)]
                
        curves.append(points)
        return curves

class l_system_fractal:
    def __init__(self , turtle : turtle , l_system : l_system , axiom : string) -> None:
        self.turtle = turtle
        self.system = l_system
        self.axiom = axiom

#科赫曲线：
def create_koch_curve():
    return l_system_fractal( turtle(1,np.pi / 3), l_system([production("f" , "f+f--f+f")]) , "f")

#科赫雪花：
def create_koch_snowflake():
    return l_system_fractal( turtle(1,np.pi / 3), l_system([production("f" , "f+f--f+f")]) , "f--f--f")

#谢尔宾斯基方毯：
def create_sierpinski_carpet():
    return l_system_fractal( turtle(1,np.pi / 2), l_system([production("f" , "f-f+f+f+h-f-f-f+f") , production("h" , "hhh")]) , "f")

#谢尔宾斯基三角：
def create_sierpinski_triangle():
    return l_system_fractal( turtle(1,np.pi / 3), l_system([production("f" , "f--f--f--gg") , production("g" , "gg")]) , "f--f--f")

#二次科赫岛：
def create_second_koch_island():
    return l_system_fractal( turtle(1,np.pi / 2), l_system([production("f" , "f+f-f-ff+f+f-f")]) , "f-f-f-f")

#Pentigree分形：
def create_pentigree():
    return l_system_fractal( turtle(1,np.pi * 0.4), l_system([production("f" , "f-f++f+f-f-f")]) , "f-f-f-f-f")

#Peano曲线(L)：
def create_peano_curve_l():
    return l_system_fractal( turtle(1,np.pi / 3), l_system([production("L" , "L-R--R+L++LL+R-") , production("R" , "+L-RR--R-L++L+R")]) , "L")

#Peano曲线(R)：
def create_peano_curve_r():
    return l_system_fractal( turtle(1,np.pi / 3), l_system([production("L" , "L-R--R+L++LL+R-") , production("R" , "+L-RR--R-L++L+R")]) , "R")

#龙曲线：
def create_dragon_curve():
    return l_system_fractal( turtle(1,np.pi / 2), l_system([production("L" , "L+R") , production("R" , "L-R")]) , "L")

#希尔伯特曲线：
def create_hilbert_curve():
    return l_system_fractal( turtle(1,np.pi / 2), l_system([production("f" , "+eg-fgf-ge+") , production("e" , "-fg+ege+gf-")]) , "f")












