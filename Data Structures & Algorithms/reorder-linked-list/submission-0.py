# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        slow.next=None
        prev=None

        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        
        start=head
        while head and prev:
            next_1=head.next
            head.next=prev
            next_2=prev.next
            prev.next=next_1
            head=next_1
            last=prev
            prev=next_2


