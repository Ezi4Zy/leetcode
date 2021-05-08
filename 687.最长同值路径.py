#
# @lc app=leetcode.cn id=687 lang=python
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.ans = 0
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def max_length(node):
            if not node:
                return 0
            left_max_length = max_length(node.left)
            right_max_length = max_length(node.right)
            left_length = right_length = 0
            if node.left and node.left.val == node.val:
                left_length = left_max_length + 1
            if node.right and node.right.val == node.val:
                right_length = right_max_length + 1
            self.ans = max(self.ans, left_length + right_length)
            return max(left_length, right_length)
        max_length(root)
        return self.ans
        
        
# @lc code=end

