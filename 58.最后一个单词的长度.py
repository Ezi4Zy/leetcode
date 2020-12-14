#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        index = -1
        while index + len(s) + 1:
            if s[index] == ' ':
                if length:
                    break
            else:
                length += 1
            index -= 1
        return length
# @lc code=end

