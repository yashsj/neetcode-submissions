# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        queue=deque([root])
        ans=[]
        if not root:
            return []
        while queue:
            curr=[]
            for i in range(len(queue)):
                node=queue.popleft()
                if i==0:
                    ans.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return ans




        