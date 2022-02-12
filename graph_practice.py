# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:56:19 2021

@author: ragha
"""

class vertex:    
    
    def __init__(self,key):
        
        self.id = key
        self.connectedTo = {}
        
    def addNeighbour(self,nbr,weight = 0):
        
        self.connectedTo[nbr] = weight
        
class Graph:
    
    def __init__(self):
        
        self.vertList = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        
        self.numVertices += 1
        
        new_vert = vertex(key)
        
        self.vertList[key] = new_vert
        
        return new_vert
    
    def addEdge(self,f,t,weight = 0):
        
        f.addNeighbour(t,weight)
        
        
        
        