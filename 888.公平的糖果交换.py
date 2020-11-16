#
# @lc app=leetcode.cn id=888 lang=python
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution(object):
    def _fair_candy_swap(self, A, B, diff):
        a = b = 0
        while True:
            if B[b] - A[a] > diff:
                a += 1
            elif B[b] - A[a] < diff:
                b += 1
            else:
                return [A[a],B[b]]
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        total = sum(A) + sum(B)
        if sum(A) > total/2:
            return self._fair_candy_swap(sorted(B), sorted(A), (sum(A) - sum(B))/2)[::-1]
        else:
            return self._fair_candy_swap(sorted(A), sorted(B), (sum(B) - sum(A))/2)

        
        
# @lc code=end

