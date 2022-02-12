"""
Created on Thu Dec 16 11:49:20 2021

@author: Ragha
"""


class push_relabel:

    def __init__(self,Cap,s,t,n,excess,height):
        
        #initialize the variables
        self.Cap = Cap  
        self.s = s
        self.t = t
        self.excess = excess
        self.height = height
    
    def Maximum_Flow(self):
        
        #initialize flow
        self.Flow = [[0] * n for i in range(n)]

        self.neighbours = [0] * n  
        self.nodelist = [i for i in range(n) if i != self.s and i != self.t]
        
        #initialize for source
        self.height[self.s] = n 
        self.excess[self.s] = float("inf")
        
        #iterate through the matrix and send flow for each val from source > 0
        for v in range(n):
            if self.Cap[self.s][v]>0:
                self.push(self.s,v)
    
        p = 0
        
        #run loop for all nodes except the source and target
        while p < len(self.nodelist):
            u = self.nodelist[p]
            old_height = self.height[u]
            flag=0
            flag=self.discharge(u)
            #bring the discharged node to the front of the list
            if self.height[u] > old_height:
                self.nodelist.insert(0, self.nodelist.pop(p))
                #print(p,self.nodelist)
                p = 0  
            else:
                p += 1
                if flag==1:
                    break
            #print(self.Flow)
        return sum(self.Flow[self.s]) #return the sum of outgoing flow from source
    #after all maximum flow has been pushed

    def push(self,u, v):
        
        #send flow only for the min val of cap flow or the excess flow
        send = min(self.excess[u], self.Cap[u][v] - self.Flow[u][v])
        
        #change flow values
        self.Flow[u][v] += send
        self.Flow[v][u] -= send
        
        #change excess values
        self.excess[u] -= send
        self.excess[v] += send
        
        #flag the if cap is greater than flow
        if self.Cap[u][v]-self.Flow[u][v]>0:
            return (1)
            
    def discharge(self,u):
        
        while self.excess[u] > 0:
            if self.neighbours[u] < n:  
                v = self.neighbours[u]
                # check next neighbour
                #call push only if u is overflowing and height(u) > height(v)
                if self.Cap[u][v] - self.Flow[u][v] > 0 and self.height[u] > self.height[v]:
                    flag=self.push(u, v)
                    if flag==1:
                        return(1)
                else:
                    self.neighbours[u] += 1
            # we have checked all neighbours -  relabel
            #when u is overflowing and for all v height(u)<height(v)
            else:
                self.relabel(u)
                self.neighbours[u] = 0
                
    def relabel(self,u):
        
        #increases the height of u
        min_height = float('inf')
        for v in range(n):
            if self.Cap[u][v] - self.Flow[u][v] > 0:
                min_height = min(min_height, self.height[v])
        self.height[u] = min_height + 1

n=5
C = [[0,0,5,3,0],
     [0,0,0,0,7],
     [0,3,0,3,3],
     [0,5,0,0,0],
     [0,0,0,0,0]]


source = 0  
sink = n-1 


excess=[0,0,0,0,0,0]
height=[0,0,0,0,0,0]
PR = push_relabel(C, source, sink,n,excess,height)
max_flow_value = PR.Maximum_Flow()
print("The Max flow is:", max_flow_value)