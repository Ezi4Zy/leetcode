#
# @lc app=leetcode.cn id=1343 lang=python
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        ret = 0
        begin = 0
        total = 0
        while begin + k - 1 < len(arr):
            if begin:
                total = total - arr[begin-1] + arr[begin+k-1]
            else:
                total = sum(arr[begin:begin+k])
            if total >= k * threshold:
                ret += 1
            begin += 1
        return ret
# @lc code=end

