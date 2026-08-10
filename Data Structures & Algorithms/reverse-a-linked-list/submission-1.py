# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=None
        while head and head.next != None:
            nextnode=head.next
            head.next=node
            node=head
            head=nextnode
        if head: head.next=node

        return head
            

        



        