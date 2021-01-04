#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.minimum_difference = None
        self.pre = None
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            if self.pre is None:
                self.pre = root.val
            else:
                if self.minimum_difference is None:
                    self.minimum_difference = root.val - self.pre
                else:
                    self.minimum_difference = min(self.minimum_difference, root.val - self.pre)
                self.pre = root.val
            self.dfs(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.minimum_difference
        
# @lc code=end

