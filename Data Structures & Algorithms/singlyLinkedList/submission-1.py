class ListNode:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next=next_node
class LinkedList:
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=self.head
    
    def get(self, index: int) -> int:
        curr=self.head.next
        i=0
        while curr:
            if i==index:
                return curr.value
            i+=1
            curr=curr.next 
        return -1

    def insertHead(self, val: int) -> None:
        curr=ListNode(val)
        curr.next=self.head.next
        self.head.next=curr
        if not curr.next:
            self.tail=curr


    def insertTail(self, val: int) -> None:
        self.tail.next=ListNode(val)
        self.tail=self.tail.next

    def remove(self, index: int) -> bool:
        i=0
        curr=self.head
        while i < index and curr:
            i+=1
            curr=curr.next
        
        if curr and curr.next:
            if curr.next==self.tail:
                self.tail=curr
            curr.next=curr.next.next
            return True 
        return False


    def getValues(self) -> List[int]:
        result=[]
        curr=self.head.next
        while curr:
            result.append(curr.value)
            curr=curr.next
        return result
