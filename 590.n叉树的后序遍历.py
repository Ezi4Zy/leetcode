#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N叉树的后序遍历
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
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            if root.children:
                for child in root.children:
                    self.postorder(child)
            self.ret.append(root.val)
        return self.ret
        
# @lc code=end

