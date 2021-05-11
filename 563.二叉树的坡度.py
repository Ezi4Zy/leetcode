#
# @lc app=leetcode.cn id=563 lang=python
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNodeA
        :rtype: int
        """
        self.ret = 0
        
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
                node.left_sum = node.left.left_sum + node.left.val + node.left.right_sum
            else:
                node.left_sum = 0
            if node.right:
                dfs(node.right)
                node.right_sum = node.right.left_sum + node.right.val + node.right.right_sum
            else:
                node.right_sum = 0
            self.ret += abs(node.left_sum - node.right_sum)
        dfs(root)
        return self.ret
# @lc code=end

