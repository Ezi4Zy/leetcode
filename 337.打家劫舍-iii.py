#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.rob(root.left)
        self.rob(root.right)
        root.rob = root.val + (root.left.not_rob if root.left else 0) + (root.right.not_rob if root.right else 0)
        root.not_rob = max((root.left.rob if root.left else 0), (root.left.not_rob if root.left else 0)) + max((root.right.rob if root.right else 0), (root.right.not_rob if root.right else 0))
        return max([root.rob, root.not_rob])
# @lc code=end

