from numbers import *
from random import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/utils'))

from geometry import *
from ifs_common import *

class IFSP2d:
  def __init__(self , omegas : list[(float , AffineTransform2d)]) -> None:
    self.omegas = omegas

  def process_point(self , point : Point2D) -> Point2D:
    ra = random()
    for omega in self.omegas:
      if ra <= omega[0]:
        return omega[1].transform(point)
      ra -= omega[0]
    return None




  
