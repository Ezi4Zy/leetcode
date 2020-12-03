#
# @lc app=leetcode.cn id=1530 lang=python
#
# [1530] 好叶子节点对的数量
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, root, distance):
        if root:
            root.left_leaf = collections.Counter()
            root.right_leaf = collections.Counter()
            if not root.left and not root.right:
                root.left_leaf[0] = 1
            if not root.left:
                left_ret = 0
            else:
                left_ret = self.dfs(root.left, distance)
                for k, v in root.left.left_leaf.iteritems():
                    root.left_leaf[k+1] += v
                for k, v in root.left.right_leaf.iteritems():
                    root.left_leaf[k+1] += v
            if not root.right:
                right_ret = 0
            else:
                right_ret = self.dfs(root.right, distance)
                for k, v in root.right.left_leaf.iteritems():
                    root.right_leaf[k+1] += v
                for k, v in root.right.right_leaf.iteritems():
                    root.right_leaf[k+1] += v
            ret = 0
            for left_k in root.left_leaf.keys():
                for right_k in root.right_leaf.keys():
                    if left_k and right_k and left_k + right_k <= distance:
                        ret += root.left_leaf[left_k] * root.right_leaf[right_k]
            return ret + left_ret + right_ret
    
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        return self.dfs(root, distance)
# @lc code=end

