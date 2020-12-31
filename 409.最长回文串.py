#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counter = collections.Counter()
        for c in s:
            char_counter[c] += 1
        flag = False
        ret = 0
        for count in char_counter.values():
            if count % 2:
                flag = True
                ret += count - 1
            else:
                ret += count
        return ret + (1 if flag else 0)
        
# @lc code=end

