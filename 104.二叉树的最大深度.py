#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dep(self, node):
        if node.left:
            self.dep(node.left)
            node.left_depth = 1 + max(node.left.left_depth, node.left.right_depth)
        else:
            node.left_depth = 1
        if node.right:
            self.dep(node.right)
            node.right_depth = 1 + max(node.right.left_depth, node.right.right_depth)
        else:
            node.right_depth = 1
            
        
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dep(root)
        return max(root.left_depth, root.right_depth)
# @lc code=end

