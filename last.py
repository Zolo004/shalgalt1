#   1_b
#   2_b
#   3_a
#   4_a
#   5_c
#   6_a
#   7_c
#   7.1_c
#   8_c
#   9_a
#   10_d
#   11_b
#   12_b
#   13_ sanah oi  massiv               : togtmol ,   list:hemjee uurchlugduhgui 
#       ugugdul hadgalah arga  massiv  : indekseer hadgalna  list:
#       hurd                           : massiv : O(1)       link :O(n)
#   14_ 
#   15_c 
#   16_a
#   17_b

#   1111111
#        def greedy_algorithm(amount):
#               coins = [25,10,5,1,]
#               coin_count ={}

#            for coin in coins:
#                if amount >= coin:
#                   count = amount // coin  
#                   coin_count[coin] = count  
#                   amount -= coin * count  

#              return coin_count

#         if __name__ == "__main__":
#               amount = int(input("mungun dun: "))  
#               result = greedy_algorithm(amount)

    
#         for coin, count in result.items():
#         print(f"{count}x{coin} coin")


#     daalgavar 111111111111         (c)  66666zoos
         

        #   def greedy_coin_change(amount):

        #         coins = [25, 10, 5, 1]
        #         coin_count = {}
    
  
        #        for coin in coins:
        #             if amount >= coin:
        #                  count = amount // coin 
        #                  coin_count[coin] = count  
        #                  amount -= coin * count  

        #        return coin_count


        # amount = 67
        # result = greedy_coin_change(amount)

        # for coin, count in result.items():
        #     print(f"{count}x{coin} coin")



#  222222222222222222  (haffman code)

import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
    
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


data = [64, 34, 25, 12, 22, 11, 90]




#3333333333333333333333333333333  O(n) 

#       3_b


#444444444444444444444444444444  binar tree


class Node:
    def __init__(self, key):
        self.left = None  
        self.right = None  
        self.val = key  

   #utga nemeh 

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key) 
            else:
                self._insert_recursively(current_node.left, key) 
        else:
            if current_node.right is None:
                current_node.right = Node(key)  
            else:
                self._insert_recursively(current_node.right, key) 

  #utga haih
      def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, current_node, key):
        if current_node is None:
            return False  
        if key == current_node.val:
            return True  
        elif key < current_node.val:
            return self._search_recursively(current_node.left, key)  
        else:
            return self._search_recursively(current_node.right, key)  
        

    #    hamgiin baga 
    def find_min(self):
        return self._find_min_recursively(self.root)

    def _find_min_recursively(self, current_node):
        if current_node.left is None:
            return current_node.val  
        return self._find_min_recursively(current_node.left)  
    

    #hamgiin ih 
    def find_max(self):
        return self._find_max_recursively(self.root)

    def _find_max_recursively(self, current_node):
        if current_node.right is None:
            return current_node.val 
        return self._find_max_recursively(current_node.right)  
    


##  4 44444444444444444444444444444444444444444444444  func butsaaah 

def test_func(x):
    if x % 2 == 0:
        return x * 2
    else:
        return x + 2

print(test_func(5))




#hariu  bbbbbb






                        
                        
