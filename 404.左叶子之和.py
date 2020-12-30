#
# @lc app=leetcode.cn id=404 lang=python
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left:
                if not root.left.left and not root.left.right:
                    left_val = root.left.val
                else:
                    left_val = self.sumOfLeftLeaves(root.left)
            else:
                left_val = 0
            if root.right:
                right_val = self.sumOfLeftLeaves(root.right)
            else:
                right_val = 0
            return left_val + right_val
        return 0
        
# @lc code=end

