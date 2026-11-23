from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        res=[]
        if not root:
            return []
        while queue:
            cur=[]
            for i in range(len(queue)): #(2)
                node=queue.popleft()
                cur.append(node.val)

            #append the node left
                if node.left:
                    queue.append(node.left)
                #append node right 
                if node.right:
                    queue.append(node.right)
            res.append(cur)
        return res





        