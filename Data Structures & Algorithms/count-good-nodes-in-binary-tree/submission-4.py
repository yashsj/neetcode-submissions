# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def helper(root,val):
            if not root:
                return 0
            
            count= 1 if val<=root.val else 0
            resmax=max(root.val,val)
            count+=helper(root.left,resmax)
            count+=helper(root.right,resmax)
            return count


        return helper(root,root.val)

        # O(N)
        # O(N)