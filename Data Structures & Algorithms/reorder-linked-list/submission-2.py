# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy=ListNode()
        dummy.next=head
        fast=slow=dummy
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        pt1=dummy.next
        pt2=slow.next
        slow.next=None
        prev=None
        while pt2:
            nextnode=pt2.next
            pt2.next=prev
            prev=pt2
            pt2=nextnode
        
        while prev:
            nextnode1=pt1.next
            pt1.next=prev
            nextnode2=prev.next
            prev.next=nextnode1
            prev=nextnode2
            pt1=nextnode1
        


