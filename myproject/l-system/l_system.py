import numpy as np
import string
import array as array
import random

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/utils'))
import stacks as stacks

class Production:
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

class L_System:
    """
    L-系统
    """
    def __init__(self , ps : array):
        self.ps = ps

    def produce(self , v : string):
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

class Turtle:
    """
    海龟
    """
    def __init__(self , d  , alpha , * , s = 1) -> None:
        self.d = d
        self.alpha = alpha
        self.s = s
        self.cos = np.cos(alpha)
        self.sin = np.sin(alpha)

    def run(self , word : string) :
        heading = np.matrix([1,0,0]).T
        length = self.d
        points = [(0,0,0)]
        position = np.matrix([0.0,0.0,0.0]).T
        curves = []
        state_stack = stacks.stack()

        for letter in word:
            if letter == "f" or letter == "g" or letter == "e" or letter == "L" or letter == "R":
                position += length * heading
                length = length * self.s
                points.append((position[0,0] , position[1,0] , position[2,0]))

            elif letter == "+":
                heading = np.matrix([[self.cos , -self.sin , 0] , [self.sin , self.cos , 0 ] , [0 , 0 , 1]]) * heading

            elif letter == "-":
                heading = np.matrix([[self.cos , self.sin , 0] , [-self.sin , self.cos , 0 ] , [0 , 0 , 1]]) * heading
                
            elif letter == "&":
                heading = np.matrix([[self.cos , 0 , -self.sin] , [0 , 1 , 0] , [self.sin , 0 , self.cos]]) * heading
                
            elif letter == "^":
                heading = np.matrix([[self.cos , 0 , self.sin] , [0 , 1 , 0] , [-self.sin , 0 , self.cos]]) * heading

            elif letter == "/":
                heading = np.matrix([[1 , 0 , 0] , [0 , self.cos , -self.sin] , [0 , self.sin , self.cos]]) * heading

            elif letter == "\\":
                heading = np.matrix([[1 , 0 , 0] , [0 , self.cos , self.sin] , [0 , -self.sin , self.cos]]) * heading

            elif letter == "h":
                curves.append(points)
                position += heading * length
                points = [(position[0,0] , position[1,0] , position[2,0])]

            elif letter == "[":
                state_stack.push((position,heading,length))

            elif letter == "]":
                state = state_stack.pop()
                position = state[0]
                heading = state[1]
                length = state[2]
                curves.append(points)
                points = [(position[0,0] , position[1,0] , position[2,0])]
                
        curves.append(points)
        return curves

class L_SystemFractal:
    def __init__(self , turtle : Turtle , l_system : L_System , axiom : string) -> None:
        self.turtle = turtle
        self.system = l_system
        self.axiom = axiom

#科赫曲线：
def create_koch_curve():
    return L_SystemFractal( Turtle(1,np.pi / 3), L_System([Production("f" , "f+f--f+f")]) , "f")

#科赫雪花：
def create_koch_snowflake():
    return L_SystemFractal( Turtle(1,np.pi / 3), L_System([Production("f" , "f+f--f+f")]) , "f--f--f")

#谢尔宾斯基方毯：
def create_sierpinski_carpet():
    return L_SystemFractal( Turtle(1,np.pi / 2), L_System([Production("f" , "f-f+f+f+h-f-f-f+f") , Production("h" , "hhh")]) , "f")

#谢尔宾斯基三角：
def create_sierpinski_triangle():
    return L_SystemFractal( Turtle(1,np.pi / 3), L_System([Production("f" , "f--f--f--gg") , Production("g" , "gg")]) , "f--f--f")

#二次科赫岛：
def create_second_koch_island():
    return L_SystemFractal( Turtle(1,np.pi / 2), L_System([Production("f" , "f+f-f-ff+f+f-f")]) , "f-f-f-f")

#Pentigree分形：
def create_pentigree():
    return L_SystemFractal( Turtle(1,np.pi * 0.4), L_System([Production("f" , "f-f++f+f-f-f")]) , "f-f-f-f-f")

#Peano曲线(L)：
def create_peano_curve_l():
    return L_SystemFractal( Turtle(1,np.pi / 3), L_System([Production("L" , "L-R--R+L++LL+R-") , Production("R" , "+L-RR--R-L++L+R")]) , "L")

#Peano曲线(R)：
def create_peano_curve_r():
    return L_SystemFractal( Turtle(1,np.pi / 3), L_System([Production("L" , "L-R--R+L++LL+R-") , Production("R" , "+L-RR--R-L++L+R")]) , "R")

#龙曲线：
def create_dragon_curve():
    return L_SystemFractal( Turtle(1,np.pi / 2), L_System([Production("L" , "L+R") , Production("R" , "L-R")]) , "L")

#希尔伯特曲线：
def create_hilbert_curve():
    return L_SystemFractal( Turtle(1,np.pi / 2), L_System([Production("f" , "+eg-fgf-ge+") , Production("e" , "-fg+ege+gf-")]) , "f")












