import math

class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.child = None
        self.p = None
        self.sibling = None

class Binomial_Heap:
    def __init__(self):
        self.header = None    

    def link_heaps(self, y, z):
        
        #link the nodes
        y.p = z
        y.sibling = z.child
        z.child = y
        z.degree = z.degree + 1
    
    def merge(self, H2):
            
        #Find length of Heap 1
        len_H1 = 0
        current_node = self.header
        while current_node != None:
            current_node = current_node.sibling
            len_H1 += 1
        
        #Find length of Heap 2
        len_H2 = 0
        current_node = H2.header
        while current_node != None:
            current_node = current_node.sibling
            len_H2 += 1
        
        #Create pointers to headers of list 1 and list 2
        current_node_H1 = self.header
        current_node_H2 = H2.header
        
        i = 1
        temp_node = Node(None)
        merged_list = temp_node
        
        
        while i <= len_H1 + len_H2:
            
            #if heap1 is empty add all elements of heap 2
            if current_node_H1 == None:
                temp_node.sibling = current_node_H2
                current_node_H2 = current_node_H2.sibling
            #if heap2 is empty add all elements of heap 1
            elif current_node_H2 == None:
                temp_node.sibling = current_node_H1
                current_node_H1 = current_node_H1.sibling
                
            #depends on the degree and merge the trees
            elif current_node_H1.degree <= current_node_H2.degree:
                temp_node.sibling = current_node_H1
                current_node_H1 = current_node_H1.sibling
            
            #merge the trees based on degrees
            elif current_node_H1.degree > current_node_H2.degree:
                temp_node.sibling = current_node_H2
                current_node_H2 = current_node_H2.sibling
                
            i = i+1
            temp_node = temp_node.sibling
        merged_list = merged_list.sibling
        return merged_list
    
    def heap_union(self, H2):
        
        #create new binomial heap
        H = Binomial_Heap()
        
        #assign the current heap to H1
        H1 = self.header
        
        #merge the header with the self 
        H.header = self.merge(H2)
        
        #delete objects if they point to None
        if H1 == None:
            del H1
        else:
            H1.header = None
            del H1
        if H2 == None:
            del H2
        else:
            H2.header = None
            del H2
            
        
        if H.header == None:
            return H
        
        #assign three pointers one to prev_x to previous, x to current and next_x to sibling of x
        prev_x = None
        x = H.header
        next_x = x.sibling
        
        #run a loop till next_x is not null
        while next_x != None:
            
            #move the pointer if the current degree is not equal to next degree
            if (x.degree != next_x.degree) or (next_x.sibling != None and next_x.sibling.degree == x.degree):
                prev_x = x
                x = next_x
                
            #if x is less link x to next_x
            elif x.key <= next_x.key:
                x.sibling = next_x.sibling
                self.link_heaps(next_x,x)
                
            
            else:
                
                # make the smaller as head and link
                if prev_x == None:
                    H.header = next_x
                    self.link_heaps(x, next_x)
                    
                #moving the pointer and linking the nodes according to the valu
                else: 
                    prev_x.sibling = next_x
                    self.link_heaps(x, next_x)
                    x = next_x
            next_x = x.sibling
        return H
    
    def insert(self, key):
        
        H2 = Binomial_Heap()
        H2.header = Node(key)
        self.header = self.heap_union(H2).header
    
    def minimum(self):
        
        #check the roots and find the minimum
        y = None
        x = self.header
        min_ = math.inf
        while x != None:
            if x.key < min_:
                min_ = x.key
                y = x
            x = x.sibling
        return y
    
    def extract_min(self):
        x = self.minimum()
        
        #Remove the Binomial Tree of root x
        
        #if the header is the min element
        if self.header == x:
            self.header = x.sibling
            
        
        else:
            current_node = self.header
            
            #move the pointer till we find the min and link the prev with the next
            while current_node.sibling != x:
                current_node = current_node.sibling
            current_node.sibling = current_node.sibling.sibling

        
        prev_node = None
        current_node = x.child
        
        #makes a heap in the reverse order
        while current_node != None:
            next_node = current_node.sibling
            current_node.sibling = prev_node
            prev_node = current_node
            current_node = next_node
        
        #Put reversed rootlist into a new binomial Heap
        H2 = Binomial_Heap()
        H2.header = prev_node
        x.child = None
        
        #make the union
        self.header = self.heap_union(H2).header
        
        return x
        
    def decrease_key(self, x, k):
        
        if k > x.key:
            return "New key has higher value current key"
        
        #assign the value
        x.key = k
        y = x
        z = y.p
        
        #move the node up
        temp = 0
        while z != None and y.key < z.key:
            temp = y.key
            y.key = z.key
            z.key = temp
            y = z
            z = y.p
        del temp
    
    def delete(self, x):
        
        #decrease key to -inf
        self.decrease_key(x, -math.inf)
        #remove the min node
        self.extract_min()
        
Heap1 = Binomial_Heap()

for i in [28,5,13,37,7,16,12,28,24,3,11,19,10,8]:
    Heap1.insert(i)
    

    
print("-----")
print(Heap1.header.key)
print(Heap1.header.child.key)
print(Heap1.header.sibling.key)
print(Heap1.header.sibling.child.key)
print(Heap1.header.sibling.child.sibling.key)
print(Heap1.header.sibling.child.child.key)
print(Heap1.header.sibling.sibling.key)
print(Heap1.header.sibling.sibling.child.key)
print("------")

t = Heap1.header

while t is not None:
    print(t.key,"<-- root")
    
    t = t.sibling
print("*****")
print(Heap1.extract_min().key,"<--- minimum")


print("******")
t = Heap1.header

while t is not None:
    print(t.key,"<-- root")
    
    t = t.sibling

print("-----")
print(Heap1.header.key)
print(Heap1.header.sibling.key) 
print(Heap1.header.sibling.child.key)
print(Heap1.header.sibling.child.sibling.key)
print(Heap1.header.sibling.child.child.key)
print(Heap1.header.sibling.sibling.key)
print(Heap1.header.sibling.sibling.child.key)
print("------")
    

# code test

print("---")
Heap1.insert(5)
print(Heap1.header.key)
print(Heap1.header.child.key)
print(Heap1.header.sibling.key) 
print(Heap1.header.sibling.child.key)

print("*****")
print(Heap1.extract_min().key,"<--- minimum")

print(Heap1.header.key)









