from numbers import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/utils'))

from geometry import *
from ifs_common import *

class IFS2d:
  def __init__(self , omegas : list[AffineTransform2d]) -> None:
    self.omegas = omegas

  def process_point(self , points : list[Point2D]) -> list[Point2D]:
    result = []
    for point in points:
      for omega in self.omegas:
        result.append(omega.transform(point))
    return result




  
