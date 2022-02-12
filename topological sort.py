# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:16:09 2021

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
        
        
    
        
    def dfs(self,u, aList, pre, post, vis):
     
        time = 0

        pre[u] = time
   
        time += 1
         
        vis[u] = 1
         
        for v in aList[u]:
            if (vis[v] == 0):
                self.dfs(v, aList, pre, post, vis)

        post[u] = time
        time += 1  
        print(pre,"**pre**")
        print(post,"**post**")
        
        
        
    def DFS(self,s):
        
        visited = [0]*9
        print(visited)
        
        pre = [0]*9
        post = [0]*9`
        
        stack = [s]
        visited[s] = 1
        count = 1
        
        while stack:
            
            n = stack.pop(-1)
            
            pre[n] = count
            count += 1
            
            if visited[n] != 1:
                visited[n] = 1
                
                
                
            for i in self.graph[n]:
                     
                if visited[i] != 1:
                    stack.append(i)
            
            
            post[n] = count
            count += 1
            print(pre,"pre")
            print(post,"post")
        
        
        
L = [(1,8),(1,2),(2,3),(4,3),(4,5),(5,6),(2,8),(7,8)]
g = Graph(L)
g.DFS(1)

"""
aList = [[] for i in range(9)]
pre = [0]*9
post = [0]*9
vis = [0]*9
g.dfs(1, aList, pre, post, vis)
"""