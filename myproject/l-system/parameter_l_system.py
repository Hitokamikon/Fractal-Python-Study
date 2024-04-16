import numpy as np
import string
import array as array
from numbers import Number
from typing import Callable

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

p1 = parameter_production(parameter("A" , []) , lambda parameter : parameter.paras[1] <= 3 , [lambda p : parameter("A" , [p.paras[0] * 2 , p.paras[0] + p.paras[1]])])
p2 = parameter_production(parameter("A" , []) , lambda parameter : parameter.paras[1] > 3 , [lambda p : parameter("B" , [p.paras[0]]) , lambda p : parameter("A" , [p.paras[0] / p.paras[1], 0]) ])
p3 = parameter_production(parameter("B" , []) , lambda parameter : parameter.paras[0] < 1 , [lambda p : parameter("C" , [])])
p4 = parameter_production(parameter("B" , []) , lambda parameter : parameter.paras[0] >= 1 , [lambda p : parameter("B" , [p.paras[0] - 1])])

system = parameter_l_system([p1, p2 , p3 , p4])

result = [parameter("B" , [2]) , parameter("A" , [3,4])]

i = 1

while i < 6:
    result = system.produce(result)

    p = ""
    for r in result:
        p += str(r)
    
    print(str(i) + " : " + p)
    i += 1