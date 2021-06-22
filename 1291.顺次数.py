#
# @lc app=leetcode.cn id=1291 lang=python
#
# [1291] 顺次数
#

# @lc code=start
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ret = []
        for i in range(1, 9):
            num = i
            for j in range(i+1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    ret.append(num)
        return sorted(ret)

        
# @lc code=end

