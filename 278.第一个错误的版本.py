#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1
        end = n
        while begin < end - 1:
            mid = (begin + end) / 2
            if isBadVersion(mid):
                end = mid
            else:
                begin = mid
        if isBadVersion(begin):
            return begin
        else:
            return begin + 1 
# @lc code=end

