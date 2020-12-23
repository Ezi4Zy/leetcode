# -*- coding: utf-8 -*-
#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 26:
            return chr(ord('A') + (n - 1) % 26)
        return self.convertToTitle((n - 1) / 26) + self.convertToTitle( (n - 1) % 26 + 1)


# @lc code=end

