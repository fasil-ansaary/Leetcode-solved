# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        solution(root, 0, res)
        return res
def solution(root, level, result):
        if root:
            if len(result) == level:
                result.append(root.val)
            solution(root.right, level+1, result)
            solution(root.left, level+1,result)
        return        