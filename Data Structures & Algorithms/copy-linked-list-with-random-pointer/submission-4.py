"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr=head
        while curr:
            nextnode=curr.next
            curr.next=Node(curr.val)
            curr.next.next=nextnode
            curr=nextnode
        curr=head
        while curr:
            nextnode=curr.next.next
            randomnode=curr.random
            if randomnode:
                curr.next.random=randomnode.next
            if nextnode:
                curr.next.next=nextnode.next
            curr=nextnode
        
        return head.next

        #TC:O(N)
        #SC:O(1) extra space




