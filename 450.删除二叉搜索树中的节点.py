#
# @lc app=leetcode.cn id=450 lang=python
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == key:
            if root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root = None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
# @lc code=end

