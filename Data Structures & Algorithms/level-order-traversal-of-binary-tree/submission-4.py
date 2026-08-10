# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        ans=[]
        if root: 
            queue.append(root)
        while queue:
            size=len(queue)
            l=[]
            while size:
                curr=queue.popleft()
                l.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                size-=1
            ans.append(l)
        return ans
        #TC:O(N)
        #SC:O(N)


        