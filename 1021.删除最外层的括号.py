#
# @lc app=leetcode.cn id=1021 lang=python
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        left = 0
        ret = ''
        for s in S:
            if s == '(':
                if left != 0:
                    ret += s
                left += 1
            else:
                left -= 1
                if left != 0:
                    ret += s
        return ret

# @lc code=end

