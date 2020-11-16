#
# @lc app=leetcode.cn id=521 lang=python
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a != b:
            return max(len(a), len(b))
        return -1
        
# @lc code=end

