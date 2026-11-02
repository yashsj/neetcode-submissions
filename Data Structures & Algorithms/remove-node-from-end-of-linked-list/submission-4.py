# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        left=dummy
        right=dummy
        dummy.next=head
        c=n
        while c:
            right=right.next
            c-=1
        
        while right.next:
            left=left.next
            right=right.next
        
        left.next=left.next.next

        return dummy.next

 
            
        
        