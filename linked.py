class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.frequency = 1

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other        

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            self.size += 1
            return

        current = self.head
        while current.next:
            if current.data == data:
                return
            current = current.next

        if current.data == data:
            return

        current.next = Node(data)
        self.size += 1

    def traverse(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next 
             
    def search(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            node = node.next
        return False                  

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(f"{current.data}({current.frequency})")
            current = current.next
        return "->".join(nodes)

    def __len__(self):
        return self.size


if __name__ == "__main__":# create a new linked list
    ll = LinkedList()

    # insert some data
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert(3)
    ll.insert(3)

    # print the linked list and its size
    print(ll)  # output: 1(2)->2(2)->3(3)
    print(len(ll))  # output: 3
