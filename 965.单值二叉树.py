#
# @lc app=leetcode.cn id=965 lang=python
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def _is_unival_tree(self, node, val):
        if node:
            return node.val == val and self._is_unival_tree(node.right, val) and self._is_unival_tree(node.left, val)
        return True
    
    def isUnivalTree(self, root, val=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._is_unival_tree(root, root.val)
# @lc code=end

