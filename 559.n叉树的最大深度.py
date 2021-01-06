#
# @lc app=leetcode.cn id=559 lang=python
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
            if root.children:
                return 1 + max([self.maxDepth(child) for child in root.children])
            return 1
        return 0

# @lc code=end

