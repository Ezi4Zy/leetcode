#
# @lc app=leetcode.cn id=345 lang=python
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        prefix = ""
        suffix = ""
        vowels = set(['a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I'])
        begin = 0
        end = len(s) - 1
        while True:
            while s[begin] not in vowels and begin < end:
                prefix += s[begin]
                begin += 1
            while s[end] not in vowels and begin < end:
                suffix += s[end]
                end -= 1
            if begin > end:
                return prefix + suffix[::-1]
            elif begin == end:
                return prefix + s[begin] + suffix[::-1]
            else:
                prefix += s[end]
                suffix += s[begin]
                begin += 1
                end -= 1
# @lc code=end

