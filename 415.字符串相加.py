#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        trans_map = {str(i): i for i in range(10)}
        ret = ""
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        flag = 0
        while index1>= 0 or index2 >= 0:
            n1 = num1[index1] if index1 >= 0 else '0'
            n2 = num2[index2] if index2 >= 0 else '0'
            cur = trans_map[n1] + trans_map[n2] + flag
            ret = str(cur % 10) + ret
            flag = cur / 10
            index1 -= 1
            index2 -= 1
        if flag:
            ret = '1' + ret
        return ret 
# @lc code=end

