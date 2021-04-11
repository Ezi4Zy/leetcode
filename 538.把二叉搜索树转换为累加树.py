#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.add_val = 0

    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            root.val += self.add_val
            self.add_val = root.val
            self.convertBST(root.left)
            
        return root
# @lc code=end

