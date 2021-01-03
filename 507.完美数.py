#
# @lc app=leetcode.cn id=507 lang=python
#
# [507] 完美数
#

# @lc code=start
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqrt_num = int(math.sqrt(num))
        if num == sqrt_num ** 2:
            end = sqrt_num
            total = sqrt_num + 1
        else:
            end = sqrt_num + 1
            total = 1
        for i in range(2, end):
            if num % i == 0:
                total += i + num / i
        return total == num
# @lc code=end

