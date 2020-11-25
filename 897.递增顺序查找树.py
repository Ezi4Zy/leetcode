#
# @lc app=leetcode.cn id=897 lang=python
#
# [897] 递增顺序查找树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.current_node.right = node
                self.current_node = node
                inorder(node.right)
        ans = self.current_node = TreeNode(None)
        inorder(root)
        return ans.right

class Solution1(object):
    
    def dfs(self, node):
        ret = []
        if node:
            if node.left:
                ret.extend(self.dfs(node.left))
            ret.append(node.val)
            if node.right:
                ret.extend(self.dfs(node.right))
        return ret
            
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node_vals = self.dfs(root)
        root = TreeNode(node_vals[0])
        pre = root
        for val in node_vals[1:]:
            node = TreeNode(val)
            pre.right = node
            pre = node
        return root
# @lc code=end

