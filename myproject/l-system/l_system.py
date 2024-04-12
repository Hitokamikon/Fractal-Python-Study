import numpy as np
import string
import array as array

class production:
    """
    产生式
    """

    def __init__(self , predecessor , successor) :
        """
        构造函数

        Parameters
        ----------
        predecessor : 前驱
        successor : 后继
        """
        self.predecessor = predecessor
        self.successor =successor



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
            for p in self.ps:
                if p.predecessor == char:
                    result += p.successor
                    findP = True
            if not findP:
                result += char
               
        return result


class turtle:

    def __init__(self , d , alpha) -> None:
        self.d = d
        self.alpha = alpha

    def run(self , word : string) :
        heading = 0
        points = [(0,0)]
        x = 0
        y = 0
        for letter in word:
            if letter == "f":
                x += self.d * np.cos(heading)
                y += self.d * np.sin(heading)
                points.append((x,y))
            elif letter == "+":
                heading += self.alpha
            elif letter == "-":
                heading -= self.alpha
        
        return points


t = turtle(1,np.pi / 3)
ls = l_system([production("f" , "f+f--f+f")])
result = "f"

count = 0
while count < 5:
    result = ls.produce("f")
    points = t.run(result)
    count = count + 1



