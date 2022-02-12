# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:29:59 2021

@author: ragha
"""
        
class Graph:
    
    def __init__(self,edges):
        
        self.edges = edges
        self.graph = {}
        
        for s,d in edges:
            
            if s in self.graph.keys():
                self.graph[s].append(d)
            else:
                self.graph[s] = [d]
                
            if d in self.graph.keys():
                self.graph[d].append(s)
            else:
                self.graph[d] = [s]
                
        print(self.graph)
        
    
    def BFS(self,s):
        
        visited = [0]*(len(self.graph.keys()))
        
        queue = []
        
        queue.append(s)
        visited[s] = 1
        while queue:
            
            n = queue.pop(0)
            print(n," ")
            
            for i in self.graph[n]:
                if visited[i] == 1:
                    continue
                else:
                    queue.append(i)
                    visited[i] = 1
                    
    def DFS(self,s):
        
        visited = [0]*(len(self.graph.keys()))
        
        stack = [s]
        visited[s] = 1
        print(s,"***")
        while stack:
            
            n = stack.pop(-1)
            
            if visited[n] != 1:
                print(n,"****")
                visited[n] = 1
            
            for i in self.graph[n]: 
                
                if visited[i] != 1:
                    stack.append(i)
                print(stack,"stack")
                
                
    def isCyclic(self):
        
        visited = [0]*(len(self.graph.keys()))

        for i in range(len(self.graph.keys())):
            
            if not self.dfs1(i,visited):
                return 0
        return 1
                
                
                
            
                
    def dfs1(self,n,visited):
        print(visited,"***visited***")
        
        if visited[n] == 1:
            return True
        if visited[n] == -1:
            return False
        
        
        
        visited[n] = -1
        for i in self.graph[n]:
            if not self.dfs1(i,visited):
                return False
            
        visited[n] = 1
                
        return True
        
            
            

                
                
            
            
                
     
        
        
if __name__ == "__main__":
        
    V = [(0,1),(1,2),(2,3),(3,4),(4,5)]
    graph = Graph(V)    
    graph.BFS(2)
    graph.DFS(2)
    graph.isCyclic()
    
    L = [(0,1),(0,2),(1,2),(2,0),(2,3)]
    g = Graph(L)
    
    print(g.isCyclic(),"*****")
    if graph.isCyclic() == 1:
        print ("Graph has a cycle")
    else:
        print ("Graph has no cycle")
        
        
    