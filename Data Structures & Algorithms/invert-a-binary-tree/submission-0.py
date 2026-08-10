# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=deque()
        queue.append(root)
        res=[]
        if not root :
            return None

        while queue:
            size=len(queue)
            while size:
                curr=queue.popleft()
                # res.append(curr.val)
                curr.left,curr.right=curr.right,curr.left
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                size-=1
        return root


        