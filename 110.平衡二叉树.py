#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def dfs(self, root):
        if root.left:
            if not self.dfs(root.left):
                return False
            else:
                root.left_depth = max(root.left.left_depth, root.left.right_depth) + 1
        else:
            root.left_depth = 1
        if root.right:
            if not self.dfs(root.right):
                return False
            else:
                root.right_depth = max(root.right.left_depth, root.right.right_depth) + 1
        else:
            root.right_depth = 1
        return max(root.left_depth, root.right_depth) - min(root.left_depth, root.right_depth) <= 1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.dfs(root)
        else:
            return True
# @lc code=end

