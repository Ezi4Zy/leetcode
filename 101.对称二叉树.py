#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def is_symmetric(self, p, q):
        if p and q:
            return p.val == q.val and self.is_symmetric(p.left, q.right) and self.is_symmetric(p.right, q.left)
        elif not p and not q:
            return True
        else:
            return False
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.is_symmetric(root.left, root.right)

# @lc code=end

