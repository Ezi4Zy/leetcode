#
# @lc app=leetcode.cn id=537 lang=python
#
# [537] 复数乘法
#

# @lc code=start
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1.split("+")
        num2 = num2.split("+")
        num1_1 = int(num1[0])
        num1_2 = int(num1[1][:-1])
        num2_1 = int(num2[0])
        num2_2 = int(num2[1][:-1])
        return str(num1_1 * num2_1 - num1_2 * num2_2) + "+" + str(num1_1 * num2_2 + num1_2 * num2_1) + "i"




# @lc code=end

