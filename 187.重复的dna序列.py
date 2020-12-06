#
# @lc app=leetcode.cn id=187 lang=python
#
# [187] 重复的DNA序列
#

# @lc code=start

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = collections.Counter()
        length = 10
        for index in range(length, len(s)+1):
            counter[s[index-length:index]] += 1
        return [key for key in counter.keys() if counter[key] > 1]
# @lc code=end

