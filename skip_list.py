# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:36:43 2021

@author: ragha
"""

import random

class Node:
    
    def __init__(self,value):
        
        self.value = value
        self.down = None
        self.right = None
        
    def __repr__(self):
        
        t = "value : {}".format(self.value)
        return t
    
class SkipList():
    
    def __init__(self):
        
        self.init = Node(-99999)
        self.fin = Node(99999)
        self.init.right = self.fin
        
        
    def coin_flip(self):
        
        s = random.randint(0, 1)
        return s
    
    def insert(self,value):
        
        new_node = Node(value)
        
        temp = self.init
       
        prev = temp
        
        while temp is not self.fin:
            
            if temp.value < new_node.value:
                
                if temp.right.value > new_node.value and temp is not None:
                    prev = temp
                    temp = temp.down
                    
                elif temp.right.value < new_node.value and temp is not None:
                    prev = temp
                    temp = temp.right
                    
                else:
                    
                    new_node.right = prev.right
                    prev.right = new_node
                    
                    
                    
                    
                    
            
            
            
            
            
            
                
                
                
                
                
                
                
                
            
            
            
        
        
        
        
        
        