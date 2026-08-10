# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
# [3,7,9,15,20]
    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.ans=[]
        self.inorder(root)
        self.pointer=-1

    def inorder(self,root):
        # if root and root.left:
        #     self.inorder(root.left,self.ans)
        # ans.append(root.val)
        # if root and root.right:
        #     self.inorder(root.right,self.ans)
        # return
        if not root:
            return
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        self.pointer+=1
        return self.ans[self.pointer]
        

    def hasNext(self) -> bool:
        return self.pointer<len(self.ans)-1
    
    #TC:O(1)--next() and hasnext()
    #SC:O(h)--height of the tree

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()