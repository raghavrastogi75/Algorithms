# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:48:38 2021

@author: ragha
"""

class Node:
    
    def __init__(self, val):
        
        self.value = val
        self.next = None
        
    def __repr__(self):
        
        s = str(self.value)
        return s
        
        
class Queue:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        
    def insert(self, val):
        
        new_node = Node(val)
        
        if self.head == None:
            
            self.head = new_node
            self.tail = new_node
            
        self.tail.next = new_node
        self.tail = new_node
        
        #print(self.head,self.tail,new_node)
       
        
        
    def remove(self):
        
        if self.tail == None:
            return "Empty"
        
        temp = self.head
        
        self.head = temp.next
        
        
        
    def __repr__(self):
        
        temp = self.head       

        s = "head -->"
        
        if self.head == None:
            return s
        
        while temp is not self.tail:
            
            s = s + " " + str(temp.value) + "-->"
            temp = temp.next
            
        s = s + str(self.tail) + "---> Tail"
        return s

        
q1 = Queue()

l = [2,3,4,5,6,7,8,9]

for i in l:
    
    q1.insert(i)
    
print(q1)

q1.remove()

print(q1)
            
        
            
        
            
        
        
            
            
    