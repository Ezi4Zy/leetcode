#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词规律
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        pattern_map = {}
        if len(s) != len(pattern):
            return False
        for index, c in enumerate(pattern):
            if c in pattern_map:
                if pattern_map[c] != s[index]:
                    return False
            else:
                if s[index] in pattern_map.values():
                    return False
                else:
                    pattern_map[c] = s[index]
        return True
# @lc code=end

