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
      HashMap={None:None}
      curr=head
      while curr:
        copy=Node(curr.val)
        HashMap[curr]=copy
        curr=curr.next
      curr=head
      while curr:
        copy=HashMap[curr]
        copy.next=HashMap[curr.next]
        copy.random=HashMap[curr.random]
        curr=curr.next
      return HashMap[head] 


