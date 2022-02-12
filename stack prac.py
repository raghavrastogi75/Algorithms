# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:04:21 2021

@author: ragha
"""

class Node:
    
    def __init__(self, val):
        
        self.value = val
        self.next = None
        
    def __repr__(self):
        
        s = str(self.value)
        return s
    
class Stack:
    
    def __init__(self):
        
        self.top = None
        self.bottom = None
        
    def insert(self,value):
        
        new_node = Node(value)
        
        if self.bottom == None:
            self.top = new_node
            self.bottom = new_node
            
        new_node.next = self.top
        self.top = new_node               
        
    def remove(self):
        
        self.top = self.top.next
        
    def __repr__(self):
        
        temp = self.top
        s = "top ---> "
        while temp is not self.bottom:
            
            s = s + str(temp.value) + "--->"
            temp = temp.next
            
        s = s + str(self.bottom)
        
        return s
    
s1 = Stack()

l = [2,3,4,5,6,7,8,9]

for i in l:
    
    s1.insert(i)
    
print(s1)

s1.remove()

print(s1)
            