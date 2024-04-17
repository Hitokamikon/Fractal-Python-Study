import numpy as np
import string
import array as array
from numbers import Number
from typing import Callable

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/utils'))
import stacks as stacks

class parameter:
    def __init__(self , letter : string , paras : list[Number]) -> None:
        self.letter = letter
        self.paras = paras

    def __str__(self) -> str:
        result = self.letter
        if len(self.paras) > 0:
            result += "("
            i = 0
            while i < len(self.paras) :
                para = self.paras[i]
                if i== len(self.paras) - 1:
                  result += str(para)
                else:
                  result += str(para) + " , "
                i += 1
            result += ")"
          
        return result

class parameter_production:
    
    def __init__(self , predecessor : parameter , condition : Callable[[parameter],bool], successor : list[Callable[[parameter],parameter]]):
        self.predecessor = predecessor
        self.condition = condition
        self.successor = successor

class parameter_l_system:
    """
    L-系统
    """
    def __init__(self , ps : list[parameter_production]):
        self.ps = ps

    def produce(self , parameters:list[parameter]):
        result = []
        for parameter in parameters:
            findP = False
            for p in self.ps:
                if findP :
                    break
                if p.predecessor.letter == parameter.letter:
                    findP = p.condition(parameter)
                    if findP:
                        i = 0
                        while i < len(p.successor):
                            result.append(p.successor[i](parameter))
                            i+=1
            if not findP:
                result.append(parameter)
               
        return result

class parameter_turtle:

    def __init__(self , d , alpha) -> None:
        self.d = d
        self.alpha = alpha

    def run(self , word : list[parameter]):
        heading = 0
        points = [(0,0)]
        x = 0
        y = 0
        curves = []
        state_stack = stacks.stack()
        for letter in word:
            if letter.letter == "f":
                x += letter.paras[0] * np.cos(heading)
                y += letter.paras[0] * np.sin(heading)
                points.append((x,y))
            elif letter.letter == "+":
                if len(letter.paras) > 0 :
                    heading += letter.paras[0]
                else:
                    heading += self.alpha
            elif letter.letter == "-":
                if len(letter.paras) > 0 :
                    heading -= letter.paras[0]
                else:
                    heading -= self.alpha
            
        curves.append(points)
        return curves
