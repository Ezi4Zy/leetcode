#
# @lc app=leetcode.cn id=894 lang=python
#
# [894] 所有可能的满二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    all_anwsers = {0: [], 1: [TreeNode(0)]}    
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in Solution.all_anwsers:
            anwser = []
            for left_count in range(N):
                right_count = N - left_count - 1
                for left in self.allPossibleFBT(left_count):
                    for right in self.allPossibleFBT(right_count):
                        root = TreeNode(0, left, right)
                        anwser.append(root)
            Solution.all_anwsers[N] = anwser
        return Solution.all_anwsers[N]     
# @lc code=end

