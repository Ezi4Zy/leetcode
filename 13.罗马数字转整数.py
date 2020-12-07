#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ret = 0
        index = 0
        while index < len(s):
            if s[index] == 'I' and index + 1 < len(s) and s[index+1] == 'V':
                ret += 4
                index += 1
            elif s[index] == 'I' and index + 1 < len(s) and s[index+1] == 'X':
                ret += 9
                index += 1
            elif s[index] == 'X' and index + 1 < len(s) and s[index+1] == 'L':
                ret += 40
                index += 1
            elif s[index] == 'X' and index + 1 < len(s) and s[index+1] == 'C':
                ret += 90
                index += 1
            elif s[index] == 'C' and index + 1 < len(s) and s[index+1] == 'D':
                ret += 400
                index += 1
            elif s[index] == 'C' and index + 1 < len(s) and s[index+1] == 'M':
                ret += 900
                index += 1
            else:
                ret += dic[s[index]]
            index+= 1
        return ret  
# @lc code=end

