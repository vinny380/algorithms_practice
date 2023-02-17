from stack import Stack

class Queue:
  #FIFO
  def __init__(self):
    #LIFO
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, item):
    self.stack1.push(item)
  
  def dequeue(self):
    while self.stack1.size() != 1:
      self.stack2.push(self.stack1.pop())
    return self.stack1.pop()
    
  def __len__(self):
    return self.stack1.size() + self.stack2.size()

  def __str__(self):
    if self.stack1.size() < self.stack2.size():
      return f"{str(self.stack2)}"
    else:
      return f"{str(self.stack1)}"

  
#   def peek(self):
#     return self.__queue[0]

#   def is_empty(self):
#     return len(self.__queue) == 0


n = Queue()

for i in range(95,100):
  n.enqueue(i)
# print(n)
print(n.dequeue())
print(n)