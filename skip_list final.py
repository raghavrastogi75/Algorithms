# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 00:00:16 2021

@author: ragha
"""
import random

class ListNode:
 
   #creating node
   def __init__(self, val):
       self.val = val
       self.next = None
       self.down = None


class Skiplist:
   def __init__(self):
       
       #creating -inf anf inf node
       node = ListNode(float('-inf'))
       node.next = ListNode(float('inf'))
       self.levels = [node]

   def lookup(self, target: int):
       
       #going to top left
       level = self.levels[-1]
       
       #traversing through the levels
       while level:
           node = level
           while node.next.val < target:
               node = node.next
           if node.next.val == target:
               return True
           level = node.down
       return False

   def insert(self, num: int):
       stack = []
       level = self.levels[-1]
       while level:
           node = level
           while node.next.val < num:
               node = node.next
        #save the level when traversing down
           stack.append(node)
           level = node.down

       #connect to the previous stacks as tails comes up
       heads = True
       down = None
       while stack and heads:
           prev = stack.pop()
           node = ListNode(num)
           node.next = prev.next
           node.down = down
           prev.next = node
           down = node
           # flip a coin to stop or continue with the next level
           heads = random.randint(0, 1)

       # add a new level if we got to the top with heads
       if not stack and heads:
           node = ListNode(float('-inf'))
           node.next = ListNode(num)
           node.down = self.levels[-1]
           node.next.next = ListNode(float('inf'))
           node.next.down = down
           self.levels.append(node)

   def delete(self, num: int):
       stack = []
       level = self.levels[-1]
       
       #find the node and save the stack when traversing
       while level:
           node = level
           while node.next.val < num:
               node = node.next
           if node.next.val == num:
               stack.append(node)
           level = node.down

       # if stack empty element not found
       if not stack:
           return False

       #connect the previous stack with the next one
       for node in stack:
           node.next = node.next.next

       # remove the top level if it's empty
       while len(self.levels) > 1 and self.levels[-1].next.next is None:
           self.levels.pop()

       return True
   
   
    
sl = Skiplist()

t = [2,3,4,5,6,7,867,34,2,23,435]

for i in t:
    sl.insert(i)
    
print(sl.lookup(4))

print(sl.delete(4))

print(sl.lookup(4))


    

   
