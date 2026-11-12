
class Node:
    def __init__ (self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hashmap={}
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def insert(self,key,value):
        newnode=Node(key,value)
        prevnode=self.tail.prev
        prevnode.next=newnode
        newnode.prev=prevnode
        newnode.next=self.tail
        self.tail.prev=newnode
        self.hashmap[key]=newnode
      

    def remove(self,key):
        node=self.hashmap[key]
        prevnode=node.prev
        nextnode=node.next
        prevnode.next=nextnode
        nextnode.prev=prevnode
        self.hashmap.pop(key) 


    def get(self,key:int)->int:
        if key not in self.hashmap:
            return -1
        
        node=self.hashmap[key]
        self.remove(key)
        self.insert(key,node.value)
        return node.value
    
    def put(self,key:int,value:int):
        if key in self.hashmap:
            self.remove(key)
        self.insert(key,value)
        
        if len(self.hashmap)>self.capacity:
            k=self.head.next.key
            self.remove(k)
    




            

        
