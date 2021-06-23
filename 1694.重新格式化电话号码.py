#
# @lc app=leetcode.cn id=1694 lang=python
#
# [1694] 重新格式化电话号码
#

# @lc code=start
class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        l = ""
        length = 0
        for c in number:
            if c.isdigit():
                if length and length % 3 == 0:
                    l += '-'
                l += c
                length += 1
        if length % 3 == 1 and length != 1:
            l = l[:-3] + '-' + l[-3] + l[-1]
        return l

# @lc code=end

