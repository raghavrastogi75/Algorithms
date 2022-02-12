# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:49:34 2021

@author: ragha
"""

class Node:
    
    
    def __init__(self,key,value):
        
        
        self.key = key
        self.value = value
        self.next = None
    
    
    def __repr__(self):        
        return "Node (%s, %s)>"%(self.key, self.value) #print node
    
class HashTable:
    
    def __init__(self,capacity):
        
        self.capacity = capacity #length of hashtable
        
        self.bucket = [None]*self.capacity #hash list
        
    def hash(self,key):
        
        hash_num = 0
            
        for i in key:
            
            hash_num = hash_num + ord(i)**2 #hash function
            
        hash_sum = hash_num % self.capacity #finding the index
        
        return hash_sum
    
    def insert(self,key):
        
        index = self.hash(key)
        
        
        
        if self.bucket[index] == None: #if no key previously add key     
            self.bucket[index] = Node(key,1)            
            return
        
        #otherwise increase count
        
        temp = self.bucket[index]
        prev = self.bucket[index]
        
        #print(temp,"temp")
        
        while temp is not None: 
            
            prev = temp
            temp = temp.next
            
            if prev.key == key:
                
                prev.value += 1
                
                return
        
        #if key not found after traversal add node
        prev.next = Node(key,1)
        
        
        
    def delete(self,key):
        
        #find the index assign the index to temp, use prev as flag
        
        index = self.hash(key)
        temp = self.bucket[index]
        prev = None
        
        #if no key
        if temp == None:
            return None
        
        #traverse the linked list until we find the key or reach the end
        
        while temp is not None and temp.key != key:
            prev = temp
            temp = temp.next
            
        #if we reach end
        if temp is None:
            return None
        
        #if we find the key
        else:
            
            #if the key is the first node with value 1
            if prev is None and temp.value == 1:
                self.bucket[index] = temp.next
                #print("here",temp.next)
            
            # if the key is the first node with value more than 1
            elif prev is None:
                temp.value -= 1
                #print("here",temp.value)
            #if the key is somewhere in the middle with 1 or more count
            else:
                if prev.value == 1:
                    prev.next = prev.next.next
                    
                else:
                    prev.value = prev.value - 1
                    
    def find(self,key):
        
        #find the node
        index = self.hash(key)
        
        temp = self.bucket[index]
        
        prev = temp
        
        #traverse till the end
        while temp is not None:
            
            prev = temp
            temp = temp.next
            
            #return upon match
            if prev.key == key:
                n = "key:" + str(key) +" value:" + str(prev.value)
                return n
        #return none if nothing found    
        return None
    
    def list_all_keys(self,s):
        t = []
        s = set(s)
        for i in s:
            
            t.append(self.find(i))
            
        return t
    
    def increase_key(self,key):
        index = self.hash(key)
        
        temp = self.bucket[index]
        
        prev = temp
        while temp is not None:
            
            prev = temp
            temp = temp.next
            
            if prev.key == key:
                prev.value += 1
                
        return "key: "+ key + "old value:" + str(prev.value - 1) + " " + "New value:" + str(prev.value)
                
                       
            
#file processing         
import re 
my_file = open("hash_file1.txt", "r")

content = my_file.read()
#print(content)`

wordList = re.sub("[^\w]", " ",  content).split()

#create a list
h1 = HashTable(len(wordList))

#insert the words
for word in wordList:   
   
    h1.insert(word)

#list all keys
#h = h1.list_all_keys(wordList)
#print(h)

#find
t1 = h1.find("a")
#print(t1,"***a***")
#find
t2 = h1.find("saves")
#print(t2,"***saves***")

#delete
h1.delete("saves")
f1 = h1.find("saves")
#print(f1,"**delete saves***")

h1.insert('aaaaaaaa')
h1.increase_key('aaaaaaaa')
h = (h1.list_all_keys(['aaaaaaaa']))
h1.delete('aaaaaaaa')
print((h1.list_all_keys(['aaaaaaaa'])))


       
            
                    
        
                    
                
                
            
        
        

            
                    
            
        
        
        
        