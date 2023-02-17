class Node:
    # Function to initialize the node object
  def __init__(self, data):
      self.data = data  # Assign data
      self.next = None

  def __str__(self):
    return str(self.data)

class Linked_List:

  def __init__(self):
    self.head = self.tail = None
    self.lista = []
    self.size = len(self.lista)


  def push_to_head(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

  def push_to_tail(self, new_data):
  
        # 1. Create a new node
    # 2. Put in the data
    # 3. Set next as None
    new_node = Node(new_data)

    # 4. If the Linked List is empty, then make the
    #    new node as head
    if self.head is None:
        self.head = new_node
        return

    # 5. Else traverse till the last node
    last = self.head
    while (last.next):
        last = last.next

    # 6. Change the next of last node
    self.tail = new_node

    self.size += 1


  def push(self, prev_node, new_data):

    if prev_node is None:
        print("The given previous node must be LinkedList.")
        return

    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    self.lista.append(new_node)
    self.size += 1


  def __str__(self):
    return f"{self.head}->{'->'.join(str(i) for i in self.lista)}->{self.tail}"

  def __len__(self):
    return self.size

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
six = Node(6)

linked = Linked_List()
linked.push_to_head(one)
linked.push(one, two)
linked.push(two, three)
print(linked)
print(len(linked))