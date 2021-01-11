#
# @lc app=leetcode.cn id=606 lang=python
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t:
            t_val = str(t.val)
            if t.left:
                t_left = '(' + self.tree2str(t.left) + ')'
            else:
                t_left = ''
            if t.right:
                t_right = ('' if t.left else '()') + '(' + self.tree2str(t.right) + ')'
            else:
                t_right = ''
            return t_val + t_left + t_right
        else:
            return ''    
# @lc code=end

