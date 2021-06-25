#
# @lc app=leetcode.cn id=1768 lang=python
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ret = ""
        for index in range(min(len(word1), len(word2))):
            ret += word1[index] + word2[index]
        ret += word1[index+1:] + word2[index+1:]
        return ret
# @lc code=end

