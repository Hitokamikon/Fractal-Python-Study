import array as array

class stack:
  def __init__ (self):
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