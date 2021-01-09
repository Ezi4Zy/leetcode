#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N叉树的前序遍历
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
    
    def __init__(self):
        self.ret = []
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            self.ret.append(root.val)
            for child in root.children:
                self.preorder(child)
        return self.ret  
# @lc code=end

