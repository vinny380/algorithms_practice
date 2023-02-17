from queue_1 import Queue

class Stack:
    def __init__(self):
        self.__queue = Queue()

    def push(self, element):
        self.__queue.enqueue(element)
        
    def is_empty(self):
        return self.__queue.is_empty()
        
    def pop(self):
        for i in range(len(self.__queue) - 1):
            popped = self.__queue.dequeue()
            self.__queue.enqueue(popped)
        return self.__queue.dequeue()
    
    def __len__(self):
        return len(self.__queue)

    def __str__(self):
      return str(self.__queue)