#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniq_chars = []
        not_uniq_chars = set()
        index = 0
        for c in s:
            if c not in not_uniq_chars:
                if c in uniq_chars:
                    uniq_chars.remove(c)
                    not_uniq_chars.add(c)
                else:
                    uniq_chars.append(c)
        if uniq_chars:
            return s.index(uniq_chars[0])
        else:
            return -1
# @lc code=end

