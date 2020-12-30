#
# @lc app=leetcode.cn id=374 lang=python
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1
        end = n
        while True:
            mid = (begin + end) / 2
            guess_num = guess(mid)
            if guess_num == 0:
                return mid
            elif guess_num == -1:
                end = mid - 1
            else:
                begin = mid + 1

# @lc code=end

