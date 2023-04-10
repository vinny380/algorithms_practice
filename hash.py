import re
import string
from linked_list import Linked_List, Node
import math

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
    print(" ".join(preprocessed))
    return preprocessed


class OpenHashTable:
    def __init__(self, size: int) -> None:
        self.table = [None] * size
        self.load_factor = 0
        self.size = size

        
    def hash_func(self, word: str) -> int:
        total=0;
        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])
        total = total % self.size
        return total


    def insert(self, word: str) -> None:
        bucket = self.hash_func(word)
        word_node = Node(word)
        
        if self.table[bucket] == None:
            self.table[bucket] = Linked_List()
            self.table[bucket].push_to_head(word_node)
        else:
            spot = self.table[bucket]
            spot.push(spot.head, word_node)

        self.load_factors()        
        while self.load_factor > 0.75:
            self.table.append(None)
            self.load_factors()

    def search(self, key: str) -> bool or int:
        pass

    def load_factors(self) -> None:
        buckets_taken = 0
        for i in self.table:
            if i != None:
                buckets_taken += 1
        self.load_factor = buckets_taken/(len(self.table))


    def load_from_file(self, file_path: str):
        words = parse_file(file_path)
        hash_table = OpenHashTable()         # Creating instance of tree
        for word in words:              # Adding all the words in the list words to the tree.
            hash_table.insert(word)
        return hash_table
        

if __name__ == '__main__':
    hashtable = OpenHashTable(10)
    hashtable.insert("OI")
    hashtable.insert('OI')
    hashtable.insert("Vinicius")
    hashtable.insert("Vinicius")
    hashtable.insert("Vinicius")
    hashtable.insert('OI')
    hashtable.insert("KVJNFKJVNDFKJ")
    hashtable.insert("LEAO")
    hashtable.insert("KVJNFKJVNDFKJ")

    
    for i in hashtable.table:
        print(i)

    print(len(hashtable.table))