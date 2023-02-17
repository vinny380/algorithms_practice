class Stack:

  def __init__(self):
    self.__stack = []

  def __str__(self):
    return str(self.__stack)

  def push(self, item):
    self.__stack.append(item)

  def pop(self):
    return self.__stack.pop()

  def size(self):
    return len(self.__stack)

  def is_empty(self):
    return len(self.__stack) == 0

  def top(self):
    return self.__stack[0]

  def __iter__(self):
    for i in self.__stack:
      return i

  def __next__(self):
    x = self.a
    self.a += 1
    return x