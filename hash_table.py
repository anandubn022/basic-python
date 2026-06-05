import random

class Hash:
    def __init__(self, bucket):
        self.__bucket = bucket  #   __ for private variable
        self.__table = [[] for _ in range(bucket)]

    def hash_function(self, key):
        return key % self.__bucket
    
    def add_key(self, key):
        index = self.hash_function(key)
        self.__table[index].append(key)

    def remove_key(self, key):
        index = self.hash_function(key)
        if key not in self.__table[index]:  #   or try except
            return
        else:
            self.__table[index].remove(key)

    def display_hash_table(self):
        for i in range(self.__bucket):
            print(f"{i} :", end=" ")
            for j in self.__table[i]:
                print(f"{j}", end=" ")
            print()

h1 = Hash(8)
arr = [32, 4, 56, 47, 21, 17]
for i in arr:
    h1.add_key(i)
h1.remove_key(arr[random.randint(0, len(arr)-1)])
h1.display_hash_table()