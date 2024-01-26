# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preOrder(self, root, lst):
        if root == None:
            return
        lst.append(root.val)
        self.preOrder(root.left, lst)
        self.preOrder(root.right, lst)
        return lst
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        return self.preOrder(root, lst)
        