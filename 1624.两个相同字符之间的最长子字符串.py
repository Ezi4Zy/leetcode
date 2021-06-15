#
# @lc app=leetcode.cn id=1624 lang=python
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = -1
        s_end = len(s) - 1
        for index, c in enumerate(s):
            if ret == -1:
                end = index + 1
            else:
                end = index + ret + 2
            other_index = s_end
            while other_index >= end:
                if s[other_index] == c:
                    ret = other_index - index - 1
                    break
                other_index -= 1
        return ret

            
# @lc code=end

