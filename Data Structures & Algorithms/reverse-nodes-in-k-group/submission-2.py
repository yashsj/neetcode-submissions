# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prevNode=dummy

        while True:
            Knode=self.findKNode(prevNode,k)
            if not Knode:
                return dummy.next
            groupNext=Knode.next
            prev,curr=Knode.next,prevNode.next
            while curr!=groupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            

            tmp=prevNode.next
            prevNode.next=Knode
            prevNode=tmp

    def findKNode(self,curr,k):
        while curr and k:
            curr=curr.next
            k=k-1
        return curr

    #TC:O(N)
    #SC:O(1)
        


