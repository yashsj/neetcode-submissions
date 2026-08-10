# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=root.val
        def maxSum(root)->int:
            if not root:
                return 0
            leftmax=max(maxSum(root.left),0)
            rightmax=max(maxSum(root.right),0)
            nonlocal res
            res=max(res,leftmax+rightmax+root.val)
            return (root.val+max(leftmax,rightmax))
            
        maxSum(root)

        return res
        