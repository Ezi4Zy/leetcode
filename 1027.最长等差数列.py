#
# @lc app=leetcode.cn id=1027 lang=python
#
# [1027] 最长等差数列
#

# @lc code=start
class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}
        max_len = 2
        for index, a in enumerate(A):
            dic[index] = {}
            for i in range(index):
                if a - A[i] in dic[i]:
                    dic[index][a - A[i]] = dic[i][a - A[i]] + 1
                    max_len = max(dic[i][a - A[i]] + 1, max_len)
                else:
                    dic[index][a - A[i]] = 2
        return max_len
# @lc code=end

