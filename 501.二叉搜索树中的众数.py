#
# @lc app=leetcode.cn id=501 lang=python
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def dfs(self, root, counter):
        if root:
            counter[root.val] += 1
            self.dfs(root.left, counter)
            self.dfs(root.right, counter)
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        counter = collections.Counter()
        self.dfs(root, counter)
        if counter:
            max_count = max(counter.values())
            for mode, count in counter.iteritems():
                if count == max_count:
                    ret.append(mode)
        return ret

# @lc code=end

