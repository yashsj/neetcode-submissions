# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Postorder=[4,5,2,6,7,3,1]
        #Recursion 
        curr=root
        ans=[]
        def dfs(curr,ans):
            if curr and curr.left:
                dfs(curr.left,ans)
            if curr and curr.right:
                dfs(curr.right,ans)
            if curr:
                ans.append(curr.val)
            return
        dfs(curr,ans)
        return ans