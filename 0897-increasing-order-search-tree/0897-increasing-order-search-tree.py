# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def inorder(self, root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            self.arr.append(root.val)
            self.inorder(root.right)

    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.inorder(root)
        T = TreeNode(0)
        cur = T

        for num in self.arr:
            cur.right = TreeNode(num)
            cur = cur.right
    
        return T.right
        
