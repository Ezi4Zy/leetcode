#
# @lc app=leetcode.cn id=671 lang=python
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        children = [root] if root else []
        children_vals = set()
        while children:
            new_children = []
            for child in children:
                children_vals.add(child.val)
                if child.left:
                    new_children.append(child.left)
                if child.right:
                    new_children.append(child.right)
            children = new_children
        if len(children_vals) > 1:
            children_vals = list(children_vals)
            children_vals.sort()
            return children_vals[1]
        return -1
# @lc code=end

