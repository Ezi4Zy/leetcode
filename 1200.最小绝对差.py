#
# @lc app=leetcode.cn id=1200 lang=python
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ret = []
        min_abs_diff = arr[-1] - arr[0]
        for index in range(len(arr) - 1):
            if arr[index+1] - arr[index] < min_abs_diff:
                min_abs_diff = arr[index+1] - arr[index]
                ret = [[arr[index], arr[index+1]]]
            elif arr[index+1] - arr[index] == min_abs_diff:
                ret.append([arr[index], arr[index+1]])
            else:
                continue
        return ret

            
        
# @lc code=end

