from queue_1 import Queue
class Stack:

  def __init__(self):
    #FIFO
    self.queue1 = Queue()
    self.queue2 = Queue()
  #LIFO
  def push(self, item):
    self.queue1.enqueue(item)

  def pop(self):
    while len(self.queue1) != 0:
      self.queue2.enqueue(self.queue1.dequeue())
    return self.queue2.dequeue()


  def __str__(self):
    if len(self.queue1) > len(self.queue2):
      return f"{str(self.queue1)}"
    else:
      return f"{str(self.queue2)}"