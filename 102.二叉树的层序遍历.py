#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
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
        self.ret = []
    
    def dfs(self, nodes):
        node_vals = []
        for node in nodes:
            node_vals.append(node.val)
        self.ret.append(node_vals)
        children = []
        for node in nodes:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        if children:
            self.dfs(children)
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            self.dfs([root])
        return self.ret
# @lc code=end

