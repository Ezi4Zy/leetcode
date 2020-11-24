#
# @lc app=leetcode.cn id=572 lang=python
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def gen_next(t):
    ret = [0] * len(t)
    j = 1
    i = 0
    while j < len(t):
        if t[j] == t[i]:
            ret[j] = i + 1
            i += 1
        else:
            i = 0
        j += 1
    return ret

class Solution(object):
    # kmp
    
    def dfs(self, node):
        return [str(node.val)] + (self.dfs(node.left) if node.left else ['leaf_left']) + (self.dfs(node.right) if node.right else ['leaf_right'])       
    

    
    def is_substring(self, s, t):
        next_array = gen_next(t)
        i = 0
        j = 0
        while i < len(s):
            if s[i] == t[j]:
                j += 1
                i += 1
            else:
                if j:
                    j = next_array[j-1]
                else:
                    i += 1
            if j == len(t):
                return True
        return False
        
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s = self.dfs(s)
        t = self.dfs(t)
        return self.is_substring(s, t)



class Solution1(object):
    # dfs
    
    def is_same(self, s ,t):
        if not s and not t:
            return True
        elif s and t:
            if s.val == t.val:
                return self.is_same(s.left, t.left) and self.is_same(s.right, t.right)
        else:
            return False
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.is_same(s, t) or (self.isSubtree(s.left, t)  if s else False)or (self.isSubtree(s.right, t) if s else False)  
# @lc code=end

