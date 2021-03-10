#
# @lc app=leetcode.cn id=720 lang=python
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = set(words)
        ret = ""
        for word in words:
            if len(word) > len(ret) or (len(word) == len(ret) and word < ret):
                if all([word[:i] in words for i in range(1, len(word))]):
                    ret = word
        return ret

# @lc code=end

