#
# @lc app=leetcode.cn id=95 lang=python
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.cache_tree = {}
    
    
    def _generate_trees(self, start, end):
        cache_key = "%s_%s" % (start, end)
        if cache_key in self.cache_tree:
            return self.cache_tree[cache_key]
        ret = []
        if start > end:
            ret = [None]
        if start == end:
            ret = [TreeNode(val=start)]
        else:
            for val in range(start, end+1):
                for left_tree in self._generate_trees(start, val-1):
                    for right_tree in self._generate_trees(val+1, end):
                        node = TreeNode(val, left=left_tree, right=right_tree)
                        ret.append(node)
        self.cache_tree[cache_key] = ret
        return ret    
        
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self._generate_trees(1, n)
        
# @lc code=end

