import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/utils'))

from geometry import *

class AffineTransform2d:
  def __init__(self , a:float , b:float , c:float , d:float , e:float , f:float) -> None:
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e
    self.f = f

  def transform(self , point : Point2D) -> Point2D:
    return Point2D(self.a * point.x + self.b * point.y + self.e , self.c * point.x + self.d * point.y + self.f)
