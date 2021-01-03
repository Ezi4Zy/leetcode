#
# @lc app=leetcode.cn id=504 lang=python
#
# [504] 七进制数
#

# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = num >= 0
        num = abs(num)
        ret = ""
        while True:
            ret = str(num % 7) + ret
            num /= 7
            if num == 0:
                break
        return ("" if flag else "-") + ret
        
# @lc code=end

