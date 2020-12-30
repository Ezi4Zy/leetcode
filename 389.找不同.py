#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter()
        for c in s:
            counter[c] += 1
        for c in t:
            if counter[c] == 0:
                return c
            counter[c] -= 1
# @lc code=end

