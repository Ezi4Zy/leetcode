#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.dfs(root.right)
            self.max_diameter =  max([self.max_diameter, 
                                      ((root.left.max_diameter + 1) if root.left else 0) + ((root.right.max_diameter + 1) if root.right else 0)])
            root.max_diameter = max([(root.left.max_diameter + 1) if root.left else 0, 
                                         (root.right.max_diameter + 1) if root.right else 0])

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        if not root:
            return 0
        self.dfs(root)
        return self.max_diameter
# @lc code=end

