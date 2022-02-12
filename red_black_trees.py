# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:07:32 2021

@author: ragha
"""

class Node:
    
    def __init__(self,value):
        
        #initilise the attributes
        self.value = value
        self.color = 1 #1 for red
        self.left = None
        self.right = None
        self.parent = None
        
    def __repr__(self):
        
        #print node
        return "Value: {} Color: {}".format(self.value,self.color)
 


class RBT():

    def __init__(self):
        
        #initialise the tree with root equal to null node
        self.NULL = Node(0)
        self.NULL.color = 0 #0 for black
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
        
        
    def insert(self,value):
        
        #assign the value to new node
        new_node = Node(value)
        new_node.color = 1 #new node is initialised to red
        new_node.parent = None
        new_node.left = self.NULL
        new_node.right = self.NULL
        
        #initialising the temp variables
        parent = None
        current = self.root
        
        #reaching to the required node
        while current != self.NULL:
            parent = current
            if current.value > new_node.value:
                
                current = current.left
                
            elif new_node.value > current.value:
                current = current.right
                
            else:
                return #value already present
            
        #assigning the parent pointer to the parent
        new_node.parent = parent
        
        
        if parent == None: #current is root
            self.root = new_node
            
            #finding if the new node lies to the left of the parent or right
        elif new_node.value > parent.value:
            
            parent.right = new_node
        else:
            parent.left = new_node
        
        #fixing the tree after the insertion
        self.fix_RBT(new_node)
            
        
    def rotate_left(self, A):
        
        #A's right child becomes the parent
        B = A.right
        
        #B's left child becomes A's right child
        A.right = B.left
        
        #changing the parent of B
        if A.left != self.NULL:
            B.left.parent = A
        
        #connecting B with the parent of A
        B.parent = A.parent
        
        #If A is root, make B the root
        if A.parent == None:
            self.root = B
            
        # assign B the same position (left/right) as A
        elif A == A.parent.left:
            A.parent.left = B
        else:
            A.parent.right = B
            
        #B's left child becomes A's right child
        B.left = A
        A.parent = B
        
        
    def rotate_right(self, A):
        
        #reverse of left rotate
        B = A.left
        A.left = B.right
        if B.right != self.NULL:
            B.right.parent = A
    
        B.parent = A.parent
        if A.parent == None:
            self.root = B
        elif A == A.parent.right:
            A.parent.right = B
        else:
            A.parent.left = B
        B.right = A
        A.parent = B
        
        
    def fix_RBT(self, new_node):
        while new_node != self.root and new_node.parent.color == 1:
            
            # check if parent node is left or right child to find uncle
            if new_node.parent == new_node.parent.parent.right:
                
                uncle = new_node.parent.parent.left # set uncle node
                
                #case1 : uncle is red, shift the color upwards and go to grandparent
                if uncle.color == 1:
                    uncle.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                    
                else:
                    #case2 : uncle is black and new node at left -> right rotate -
                    #and assign new node to parent
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                        
                    #case3 : uncle is black the new node is at right -> 
                    #change the color of the parent
                    #change color of grandparent
                    
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self.rotate_left(new_node.parent.parent)
            else:
                
                #parent node is the left child 
                uncle = new_node.parent.parent.right  
                
                #case1 : uncle is red, shift the color upwards and go to grandparent
                if uncle.color == 1:
                    #case1
                    uncle.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                
                else:
                    #case2 : uncle is black and new node at left -> right rotate
                    #and assign new node to parent
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                        
                    #case3 : uncle is black the new node is at right -> 
                    #change the color of the parent
                    #change color of grandparent
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self.rotate_right(new_node.parent.parent)
        self.root.color = 0
        
    def predecessor(self,  x):
        
        #find the node
        temp = self.searchTree(x)
        if temp == "False":
            return "Invalid"
        
        #if left is not null go to the max to left
        if (temp.left != self.NULL):
            return self.maximum(temp.left)

        #traverse up till we reach a right child and return the parent of it
        y = temp.parent
        while y != self.NULL and temp == y.left:
            temp = y
            y = y.parent

        return y
        
        
    def successor(self, x):
        
        temp = self.searchTree(x) 
        if temp == "False":
            return "Invalid"             
        
        #if right is not null go to the min in right
        if temp.right != self.NULL:
            return self.minimum(temp.right)
        
        
        #traverse up till the current node is a left child and return parent of it
        y = temp.parent
        while y != self.NULL and temp == y.right:
            temp = y
            y = y.parent
        return y
    
    def maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node
    
    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node
    
    def searchTree(self, k):
        
        temp = self.root        
        parent = temp
        
        while temp != self.NULL:            
            parent = temp
            
            if temp.value < k:                
                temp = temp.right
                
            elif temp.value > k:                
                temp = temp.left
                
            else:                
                return temp
            
        
        if parent.value == k:
            return parent
        else:
            return False
        
    def print_node( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.value ) + "(" + s_color + ")" )
            self.print_node( node.left , indent , False )
            self.print_node( node.right , indent , True )

    # Function to call print
    def print_tree(self):
        self.print_node( self.root , "" , True )
        
    def sort_helper(self, node,t):
        if node != self.NULL:
            self.sort_helper(node.left,t)
            t.append((node.value))
            self.sort_helper(node.right,t)
            return t
        
    def sort(self):
        t = []
        m = self.sort_helper(self.root, t)
        return m
    
    def height(self,node):
        if node == None :
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left,right) + 1
    
myfile=open("rbt.txt","r")
content=myfile.read().split(",")
l=[]
for i in content:
    l.append(int(i))

r1=RBT()

t = l[::-1]
for i in l:
    r1.insert(i)

r1.print_tree()

while True:
    
    user = int(input("What would you like to do ?1.Insert x,2. Sortx,3.Searchx , 4.Predecessor of x, 5.Successor of x,6. Minimum Element,7. Maximum Element"))
    
    #userinteraction
    
    if user == 1:
        user=int(input("Enter value to be inserted"))
        r1.insert(user)
        r1.print_tree()
        ht=r1.height(r1.root)
        print("The height of the tree is",ht)
        
    elif user==2:
        m=r1.sort()
        print(m)
        ht=r1.height(r1.root)
        print("The height of the tree is",ht)
    elif user == 3:
        
        user = int(input("Enter value to be searched"))
        output=r1.searchTree(user)
        
        if output!=False:
            print("Element exists in the tree")
        else:
            print("Element do not exist in the tree")
            ht=r1.height(r1.root)
            print("The height of the tree is",ht)
        
    elif user==4:
        
        user=int(input("Enter value whose predecessor is to be returned"))
        output=r1.predecessor(user)
        print(output)
        ht=r1.height(r1.root)
        print("The height of the tree is",ht)
        
    elif user==5:
        user=int(input("Enter value whose successor is to be returned"))
        output=r1.successor(user)
        print(output)
        ht=r1.height(r1.root)
        print("The height of the tree is",ht)
        
    elif user==6:
        val=r1.minimum(r1.root)
        print(val.value)
        ht=r1.height(r1.root)
        print("The height of the tree is",ht)
        
    elif user==7:
        val=r1.maximum(r1.root)
        print(val.value)
        ht=r1.height(r1.root)
        print("The height of the tree is",ht)
        
    user = None

     

                
    
                
                
        
        
        
        
        
        
        
                
        
        
        