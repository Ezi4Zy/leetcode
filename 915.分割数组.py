#
# @lc app=leetcode.cn id=915 lang=python
#
# [915] 分割数组
#

# @lc code=start
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = 0
        max_a = A[index]
        while True:
            if max_a > A[index+1]:
                index += 1
            else:
                if max_a <= min(A[index+1:]):
                    return index+1
                else:
                    index += 1
                    max_a = A[index]

        
# @lc code=end

