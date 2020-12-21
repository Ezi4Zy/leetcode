#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            if not root.left and not root.right:
                return root.val == sum
            else:
                return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        else:
            return False

# @lc code=end

