import re
import string
from linked import LinkedList, Node

def parse_file(file: str) -> list:
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


def parse_list(unparsed_list: list) -> list:
    preprocessed = []
    for word in unparsed_list:
        word = word.strip().lower()
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = re.sub('\d+','', word)
        word = re.sub(' +', ' ', word)
        if word:
            preprocessed.extend(word.split(" "))
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

    def search(self, key: str) -> tuple:
        bucket_number = self.hash_func(key)

        bucket = self.table[bucket_number]

        if bucket is not None:
            start = bucket.head
            steps = 0
            while start:
                steps+=1
                if start.data == key:
                    return start.frequency, steps
                start = start.next 
        else:
            return -1

    def search_list(self, unparsed_list:list) -> None:
        new_list = parse_list(unparsed_list)
        for word in new_list:
            n = self.search(word)  
            if n is not None:
                print(word)
                print(f'Frequency: {n[0]}, Search steps: {n[1]}\n')       


    def load_factors(self) -> None:
        buckets_taken = 0
        for i in self.table:
            if i != None:
                buckets_taken += 1
        self.load_factor = buckets_taken/(len(self.table))


    def __str__(self) -> str:
        return f"{'->'.join(str(i) for i in self.table[:])}"  


    def load_from_file(self, file_path: str) -> 'OpenHashTable':
        words = parse_file(file_path)
        hashtable = OpenHashTable(self.size)
        for word in words:              # Adding all the words in the list words to the tree.
            hashtable.insert(word)
        return hashtable


if __name__ == '__main__':
    hashtable = OpenHashTable(100)
    loaded_hash = hashtable.load_from_file('A3test.txt')
   
    K10 = ['research', 'lead', 'sole', 'supplement', 'best', 'too', 'obtained', 'academic', 'ethical', 'reputable']
    K20 = ['verify', 'source', 'supplement', 'assignment', 'response', 'limitations', 'irrelevant', 'integrity', 'process', 'effort', 'obtained', 'ChatGPT', 'ethical', 'information', 'pasting', 'incomplete', 'ask', 'completing', 'reputable', 'sources']
    K30 = ['content,', 'academic', 'responses.', 'supplement', 'broad,', 'verify', 'critically', 'source.', 'ethics', 'questions', 'relevant', 'limitations', 'necessary', 'ChatGPT', 'obtained', 'words', 'process', 'plagiarism,', 'integrity', 'response', 'analyze', 'information', 'open-ended', 'incomplete', 'irrelevant', 'sources', 'ethical', 'reputable', 'assignment', 'accuracy']
    K40 = ['verify', 'relevant', 'limitations', 'plagiarism,', 'reputable', 'supplement', 'pasting', 'academic', 'broad,', 'incomplete', 'process', 'critically', 'ethical', 'source.', 'integrity', 'irrelevant', 'ChatGPT', 'response', 'words', 'questions', 'completing', 'ask', 'obtained', 'information', 'ethics', 'analyze', 'necessary', 'accuracy', 'research', 'open-ended', 'assignment', 'effort', 'content,', 'sources', 'lead', 'sole', 'best', 'too']
    K50 = ['verify', 'necessary', 'source.', 'process', 'limitations', 'critically', 'incomplete', 'supplement', 'ethical', 'integrity', 'pasting', 'completing', 'obtained', 'academic', 'ChatGPT', 'questions', 'research', 'assignment', 'accuracy', 'response', 'ethical', 'effort', 'reputable', 'analyze', 'information', 'open-ended', 'irrelevant', 'words', 'sources', 'plagiarism,', 'ask', 'relevant', 'content,', 'lead', 'sole', 'best', 'too', 'ethical', 'ChatGPT', 'words', 'process', 'assignment', 'supplement', 'research', 'obtained']

    loaded_hash.search_list(K10)