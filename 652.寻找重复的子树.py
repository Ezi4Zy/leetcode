#
# @lc app=leetcode.cn id=652 lang=python
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        dic = {}
        ret = []
        def dfs(node):
            if not node:
                return '#'
            dfs_ = '%s,%s,%s' % (node.val, dfs(node.left), dfs(node.right))
            if dfs_ in dic:
                dic[dfs_] += 1
            else:
                 dic[dfs_] = 1
            if dic[dfs_] == 2:
                ret.append(node)
            return dfs_
        dfs(root)
        return ret
        
# @lc code=end

