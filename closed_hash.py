import re
import string
from linked import LinkedList, Node

def parse_file(file):
    with open(file, 'r') as input:
        content = input.readlines()
    preprocessed = []
    for line in content:
        line = line.strip().lower()
        #remove punctuation
        line = line.translate(str.maketrans('', '', string.punctuation))
        #remove stop words that care no specific meaning
        #remove numbers
        line = re.sub('\d+','', line)
        #remove extra white space
        line = re.sub(' +', ' ', line)
        if line:
            preprocessed.extend(line.split(" "))
    print(" ".join(preprocessed))
    return preprocessed

class ClosedHashTable:
    def __init__(self, size: int) -> None:
        self.table = [None] * size
        self.load_factor = 0
        self.size = len(self.table)

        
    def hash_func(self, word: str) -> int:
        total=0
        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])
        total = total % self.size
        return total


    def insert(self, word: str) -> None:
        bucket = self.hash_func(word)
        a = bucket
        word_node = Node(word)
        probing_step = 0

        if (self.table[bucket] is not None):
            spot = self.table[bucket]
            start = spot.head          
            while start:
                if start.data == word_node.data:
                    start.frequency += 1
                elif (start.deleted == True):
                    start.data = word_node
                    start.deleted = False
                    start.frequency = 1  
                start = start.next
                        
            return                    


        while ((probing_step < self.size) and (self.table[a] is not None) and (self.table[a].deleted != True)):
            probing_step += 1
            a = (bucket + probing_step) % self.size     

        if (self.table[a] is None):
            self.table[a] = LinkedList()
            self.table[a].insert(word_node)                  


    def search(self, key: str) -> int:
        bucket_number = self.hash_func(key)
        probing_step = 0
        a = bucket_number
        bucket = self.table[bucket_number]

        if bucket is not None:

            while ((probing_step < self.size) and (self.table[a] is not None)):
                probing_step += 1
                a = (bucket_number + probing_step) % self.size     

            start = bucket.head
            while start:
                if start.data == key:
                    return start.frequency
                start = start.next 
        else:
            return -1

    def __str__(self) -> str:
        return f"{'->'.join(str(i) for i in self.table[:])}"              


    def delete(self, value):
        bucket_number = self.hash_func(value)
        probing_step = 0
        a = bucket_number
        bucket = self.table[bucket_number]

        if bucket is not None:
            while ((probing_step < self.size) and (self.table[a] is not None)):
                probing_step += 1
                a = (bucket_number + probing_step) % self.size     

            start = bucket.head
            while start:
                if start.data == value:
                    start.data = ''
                    start.deleted = True
                    start.frequency = 0
                    break
                start = start.next             


    def load_from_file(self, file_path: str):
        words = parse_file(file_path)
        hashtable = ClosedHashTable(self.size)
        for word in words:              # Adding all the words in the list words to the tree.
            hashtable.insert(word)
        return hashtable


if __name__ == '__main__':
    hashtable = ClosedHashTable(10)
    j = hashtable.load_from_file('A3test.txt')
    # print(j)
    lista = my_list = ['while', 'chatgpt', 'can', 'be', 'a', 'helpful', 'resource', 'for', 'answering', 'questions']
    for n in lista:
        print(n)
        print(j.search(n), '\n') 


    # for i in hashtable.table:
    #     print(i)
