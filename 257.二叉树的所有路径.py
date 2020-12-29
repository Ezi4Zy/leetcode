#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            if not root.left and not root.right:
                return [str(root.val)]
            else:
                prefix = str(root.val) + "->"
                return [(prefix + next_) for next_ in (self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right))]
        return []
# @lc code=end

