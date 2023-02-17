class Queue:

  def __init__(self):
    self.__queue = []

  def enqueue(self, item):
    self.__queue.append(item)
  
  def dequeue(self):
    n = self.__queue[0]
    del self.__queue[0]
    return n

  def peek(self):
    return self.__queue[0]

  def is_empty(self):
    return len(self.__queue) == 0
  
  def __len__(self):
    return len(self.__queue)

  def __str__(self):
    return str(self.__queue)