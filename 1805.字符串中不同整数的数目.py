#
# @lc app=leetcode.cn id=1805 lang=python
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        number_set = set()
        number = ""
        for c in word:
            if c.isdigit():
                number += c
            else:
                if number:
                    number_set.add(int(number))
                number = ""
        else:
            if number:
                number_set.add(int(number))
        return len(number_set)

# @lc code=end

