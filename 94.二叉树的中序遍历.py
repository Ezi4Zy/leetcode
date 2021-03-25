#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            ret.append(root.val)
            stack.pop()
            root = root.right
        return ret
            
    
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root:
            ret.extend(self.inorderTraversal(root.left))
            ret.append(root.val)
            ret.extend(self.inorderTraversal(root.right))
        return ret
# @lc code=end

