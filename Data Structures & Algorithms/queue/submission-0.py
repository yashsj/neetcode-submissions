class Node:
    def __init__(self,value):       
        self.next=None
        self.prev=None
        self.value=value
class Deque:
    
    def __init__(self):
        self.head=Node(-1)
        self.tail=Node(-2)
        self.head.next=self.tail
        self.tail.prev=self.head

    def isEmpty(self) -> bool:
        if self.head.next==self.tail:
            return True
        return False

    

    def append(self, value: int) -> None:
       new_node=Node(value)
       last_node=self.tail.prev
       last_node.next=new_node
       new_node.prev=last_node
       new_node.next=self.tail
       self.tail.prev=new_node
        



    def appendleft(self, value: int) -> None:
        new_node=Node(value)
        first_node=self.head.next

        new_node.next=first_node
        first_node.prev=new_node
        self.head.next=new_node
        new_node.prev=self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            last_node=self.tail.prev
            val=last_node.value
            last_node.prev.next=self.tail
            self.tail.prev=last_node.prev
            
            return val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            first_node=self.head.next
            value=first_node.value
            first_node.next.prev=self.head
            self.head.next=first_node.next
            return value 


        
