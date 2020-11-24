#
# @lc app=leetcode.cn id=1614 lang=python
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                max_depth = max(max_depth, len(stack))
                stack.pop()
        return max_depth
            
# @lc code=end

