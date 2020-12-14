#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        index = len(digits) - 1
        while index >= 0:
            cur = digits[index] + flag
            digits[index], flag = cur % 10, cur / 10
            index -= 1
            if not flag:
                break
        if flag:
            return [1] + digits
        else:
            return digits
# @lc code=end

