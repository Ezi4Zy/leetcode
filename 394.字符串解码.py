#
# @lc app=leetcode.cn id=394 lang=python
# 
# [394] 字符串解码
# 

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        for cur, c in enumerate(s):
            if c == ']':
                pre = ret.rfind('[')
                digit_index_end = pre
                digit_index_start = pre - 1
                while ret[digit_index_start].isdigit():
                    digit_index_start -= 1
                ret = ret[:digit_index_start+1] + ret[pre+1:] * int(ret[digit_index_start+1:digit_index_end])
            else:
                ret += c
            print ret
        return ret


# @lc code=end

