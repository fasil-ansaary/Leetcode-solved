# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder_check(root, result):
        if root.left != None:
            inorder_check(root.left, result)
        result.append(root.val)
        if root.right != None:
            inorder_check(root.right, result)
        return result

class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root != None:
            return inorder_check(root, result)
        else:
            return result

    
        