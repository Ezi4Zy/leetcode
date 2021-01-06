#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = ""
        index = 0
        while index < len(s):
            ret += s[index:index+k][::-1] + s[index+k:index+2*k]
            index += 2 * k
        return ret
# @lc code=end

