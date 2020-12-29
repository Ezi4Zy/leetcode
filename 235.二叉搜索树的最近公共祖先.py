#
# @lc app=leetcode.cn id=235 lang=python
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        left_node = p if p.val < q.val else q
        right_node = q if left_node == p else p
        if root.val >= left_node.val and root.val <= right_node.val:
            return root
        elif root.val < left_node.val:
            return self.lowestCommonAncestor(root.right, left_node, right_node)
        else:
            return self.lowestCommonAncestor(root.left, left_node, right_node)

class Solution1(object):
    
    def is_common_ancestor(self, root, node):
        if root:
            if root == node:
                return True
            else:
                return self.is_common_ancestor(root.left, node) or self.is_common_ancestor(root.right, node)
        else:
            return False
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if self.is_common_ancestor(root.left, p) and self.is_common_ancestor(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if self.is_common_ancestor(root.right, p) and self.is_common_ancestor(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return root
            
# @lc code=end

