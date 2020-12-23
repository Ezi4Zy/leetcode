#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin = 0
        end = len(numbers) - 1
        while begin < end:
            if numbers[begin] + numbers[end] == target:
                return [begin + 1, end + 1]
            elif numbers[begin] + numbers[end] > target:
                end -= 1
            else:
                begin += 1
        return []
# @lc code=end

