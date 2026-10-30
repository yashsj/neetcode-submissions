# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=None
        while(head and head.next!=None):
            nextnode=head.next
            head.next=cur
            cur=head
            head=nextnode
        
        if cur:
            head.next=cur
        
        return head

        