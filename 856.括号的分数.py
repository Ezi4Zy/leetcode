#
# @lc app=leetcode.cn id=856 lang=python
#
# [856] 括号的分数
#

# @lc code=start
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for c in s:
            if c == ')':
                if stack[-1] == '(':
                    stack.pop()
                    num = 1
                    while stack and stack[-1] != '(':
                        num += stack[-1]
                        stack.pop()
                    stack.append(num)
                else:
                    num = stack[-1] * 2
                    stack.pop()
                    stack.pop()
                    while stack and stack[-1] != '(':
                        num += stack[-1]
                        stack.pop()
                    stack.append(num)
            else:
                stack.append(c)
        return stack[0]

# @lc code=end

