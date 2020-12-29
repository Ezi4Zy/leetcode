#
# @lc app=leetcode.cn id=344 lang=python
#
# [344] 反转字符串
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        begin = 0
        end = len(s) - 1
        while begin < end:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1
# @lc code=end

