#
# @lc app=leetcode.cn id=459 lang=python
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        sub_string_len = length / 2
        while sub_string_len:
            if length % sub_string_len == 0:
                for index in range(0, length-sub_string_len, sub_string_len):
                    if s[index:index+sub_string_len] != s[index+sub_string_len:index+2*sub_string_len]:
                        break
                else:
                    return True    
            sub_string_len -= 1
        return False
        
# @lc code=end

