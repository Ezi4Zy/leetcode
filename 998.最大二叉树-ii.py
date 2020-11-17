#
# @lc app=leetcode.cn id=998 lang=python
#
# [998] 最大二叉树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def _insert(self, root, node):
        if not root:
            return node
        if node.val > root.val:
            node.left = root
            return node
        else:
            root.right = self._insert(root.right, node)
            return root
            

    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = TreeNode(val)
        root = self._insert(root, node)
        return root
        
# @lc code=end

