#
# @lc app=leetcode.cn id=653 lang=python
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def search(self, root, n):
        if root:
            if root.val == n:
                return True
            elif root.val > n:
                return self.search(root.left, n)
            else:
                return self.search(root.right, n)
        else:
            return False
    
    def dfs(self, root, node, k):
        if node:
            if k - node.val != node.val:
                if self.search(root, k - node.val):
                    return True
            return self.dfs(root, node.left, k) or self.dfs(root, node.right, k)
        return False
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.dfs(root, root, k)  
# @lc code=end

