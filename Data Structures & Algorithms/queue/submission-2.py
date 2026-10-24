class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

class Deque:
    
    def __init__(self):
        self.head=Node(-1)
        self.tail=Node(-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def isEmpty(self) -> bool:
        if self.head.next==self.tail:
            return True
        return False

        
    def append(self, value: int) -> None:
        newnode=Node(value)
        lastnode=self.tail.prev
        lastnode.next=newnode
        newnode.prev=lastnode
        self.tail.prev=newnode
        newnode.next=self.tail

    def appendleft(self, value: int) -> None:
        newnode=Node(value)
        firstnode=self.head.next
        firstnode.prev=newnode
        newnode.next=firstnode
        self.head.next=newnode
        newnode.prev=self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        lastnode=self.tail.prev
        val=lastnode.value
        lastnode.prev.next=lastnode.next
        self.tail.prev=lastnode.prev
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        firstnode=self.head.next
        val=firstnode.value
        self.head.next=firstnode.next
        firstnode.next.prev=firstnode.prev
        return val

