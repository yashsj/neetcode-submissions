# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       hashmap={val:index for index,val in enumerate(inorder)} 
       self.index=0

       def dfs(l,r):
            if l>r:
                return None
            value=preorder[self.index]
            self.index+=1
            root=TreeNode(value)
            mid=hashmap[value]
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root

       return dfs(0,len(inorder)-1) 
       #TC:O(N)
       #SC:O(N)
