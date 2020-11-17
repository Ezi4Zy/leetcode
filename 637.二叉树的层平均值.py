#
# @lc app=leetcode.cn id=637 lang=python
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def get_average_and_children(self, nodes):
        vals = [node.val for node in nodes]
        children = []
        average_val = float(sum(vals)) / float(len(vals))
        for node in nodes:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        return average_val, children

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        nodes = [root]
        while True:
            average_val, children = self.get_average_and_children(nodes)
            ret.append(average_val)
            if children:
                nodes = children
            else:
                return ret

        
# @lc code=end

