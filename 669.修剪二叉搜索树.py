#
# @lc app=leetcode.cn id=669 lang=python
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if root:
            if root.val < low:
                root = root.right
                return self.trimBST(root, low, high)
            if root.val > high:
                root = root.left
                return self.trimBST(root, low, high)
            root.left = self.trimBST(root.left, low, high)
            root.right =self.trimBST(root.right, low, high)
        return root

# @lc code=end

