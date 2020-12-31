#
# @lc app=leetcode.cn id=405 lang=python
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_str = '0123456789abcdef'
        int_max = 2 ** 32
        ret = ""
        flag = num >= 0 
        num = num if flag else (int_max + num)
        while True:
            ret = hex_str[num % 16] + ret
            num /= 16
            if num == 0:
                break
        return ret
# @lc code=end

