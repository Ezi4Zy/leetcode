#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def bfs(self, nodes):
        nodes = [node for node in nodes if node]
        vals = [node.val for node in nodes]
        if vals:
            next_nodes = []
            for node in nodes:
                next_nodes.extend([node.left, node.right])
            return self.bfs(next_nodes) + [vals]
        else:
            return []
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.bfs([root])
# @lc code=end

