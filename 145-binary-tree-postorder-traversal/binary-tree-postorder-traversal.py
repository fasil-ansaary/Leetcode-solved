# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postOrder(self, root, lst):
        if root == None:
            return
        self.postOrder(root.left, lst)
        self.postOrder(root.right,lst)
        lst.append(root.val)
        return lst
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        return self.postOrder(root,lst)
            
        