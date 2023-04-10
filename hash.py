import re
import string
from linked import LinkedList, Node

def parse_file(file: str) -> str:
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
    # print(" ".join(preprocessed))
    return preprocessed

class OpenHashTable:
    def __init__(self, size: int) -> None:
        self.table = [None] * size
        self.load_factor = 0
        self.size = len(self.table)

        
    def hash_func(self, word: str) -> int:
        total=0;
        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])
        total = total % self.size
        return total


    def insert(self, word: str) -> None:
        bucket = self.hash_func(word)
        word_node = Node(word)

        if self.table[bucket] is not None:
            spot = self.table[bucket]
            start = spot.head

            while start:
                if start.data == word_node.data:
                    start.frequency += 1
                start = start.next

            spot.insert(word_node)
        else:
            self.table[bucket] = LinkedList()
            self.table[bucket].insert(word_node)
 

        self.load_factors()
        while self.load_factor > 0.75:
            self.table.append(None)
            self.load_factors()

    def search(self, key: str) -> int:
        bucket_number = self.hash_func(key)

        bucket = self.table[bucket_number]

        if bucket is not None:
            start = bucket.head
            while start:
                if start.data == key:
                    return start.frequency
                start = start.next 
        else:
            return -1


    def load_factors(self) -> None:
        buckets_taken = 0
        for i in self.table:
            if i != None:
                buckets_taken += 1
        self.load_factor = buckets_taken/(len(self.table))


    def __str__(self) -> str:
        return f"{'->'.join(str(i) for i in self.table[:])}"  


    def load_from_file(self, file_path: str):
        words = parse_file(file_path)
        hashtable = OpenHashTable(self.size)
        for word in words:              # Adding all the words in the list words to the tree.
            hashtable.insert(word)
        return hashtable


if __name__ == '__main__':
    hashtable = OpenHashTable(100)
    j = hashtable.load_from_file('A3test.txt')
    lista = my_list = ['while', 'chatgpt', 'can', 'be', 'a', 'Vinicius', 'Alice', 'Bro', 'Jax', 'Sao']
    for n in lista:
        print(n)
        print(j.search(n), '\n')