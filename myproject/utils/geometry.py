
class Point2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
 
    def __str__(self):
        return f"({self.x}, {self.y})"
 
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)
 
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y