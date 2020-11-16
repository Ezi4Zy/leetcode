#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _build(self, preorder, inorder):
        root = None
        if preorder:
            root = TreeNode()
            root.val = preorder[0]
            index = inorder.index(root.val)
            left_tree_inorder = inorder[:index]
            right_tree_inorder = inorder[index+1:]
            left_tree_length = len(left_tree_inorder)
            left_tree_preorder = preorder[1:left_tree_length+1]
            right_tree_preorder = preorder[left_tree_length+1:]
            root.left = self._build(left_tree_preorder, left_tree_inorder)
            root.right = self._build(right_tree_preorder, right_tree_inorder)
            
        return root


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = self._build(preorder, inorder)
        return root
# @lc code=end

