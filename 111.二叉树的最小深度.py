#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
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
        if not root.left and not root.right:
            return 1
        depth = 10 ** 5
        if root.left:
            depth = min(depth, self.dfs(root.left))
        if root.right:
            depth = min(depth, self.dfs(root.right))
        return depth + 1
            
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.dfs(root)
        else:
            return 0
        
# @lc code=end

