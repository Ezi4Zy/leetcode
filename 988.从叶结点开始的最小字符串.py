#
# @lc app=leetcode.cn id=988 lang=python
#
# [988] 从叶结点开始的最小字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.answer = chr(ord('z') + 1)
        def dfs(node, A):
            if not node:
                return
            A.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                self.answer = min(self.answer, "".join(A[::-1]))
            dfs(node.left, A)
            dfs(node.right, A)
            A.pop()
        dfs(root, [])
        return self.answer

        
# @lc code=end

