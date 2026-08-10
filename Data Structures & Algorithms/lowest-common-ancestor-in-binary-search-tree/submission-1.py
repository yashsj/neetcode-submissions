# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr=root
        while curr:
            if p.val>curr.val and q.val>curr.val:
                curr=curr.right
            elif p.val<curr.val and q.val<curr.val:
                curr=curr.left
            else:
                return curr
            #p and q will both exist in the BST.
            #TC:O(h) height of tree(logn or n) as only 1 node will be visited at every level
            #SC:O(1)


        