# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:25:08 2021

@author: ragha
"""

class Node:
    
    def __init__(self,value):
        
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        
    def __repr__(self):
        
        s = str(self.value)
        return s        
    

class BST:
    
    def __init__(self):
        
        self.root = None
        
    
    def search(self,value):
        
        if self.root == None:
            return "False"
        
        temp = self.root
        
        while temp is not None:
            
            if value > temp.value:
                
                temp = temp.right
            
            elif value < temp.value:
                
                temp = temp.left
                
            else:
                return temp
            
            
        return "False"
    
    def print_tree(self ,node = self.root):
        
        if node is not None:   
            
            self.print_tree(node.left)
            print(node)
            self.print_tree(node.right)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
   
    