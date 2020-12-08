#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin = 0
        end = 1
        ret = min(len(s), 1)
        while end < len(s):
            if s[end] in s[begin:end]:
                ret = max(ret, (end-begin))
                begin += s[begin:end].index(s[end]) + 1
            end += 1
            if end == len(s):
                ret = max(ret, (end-begin))
                break
        return ret
            
# @lc code=end

