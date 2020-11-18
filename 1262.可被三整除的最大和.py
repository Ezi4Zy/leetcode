#
# @lc app=leetcode.cn id=1262 lang=python
#
# [1262] 可被三整除的最大和
#

# @lc code=start

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        state = [0, 0, 0]
        for num in nums:
            if num % 3 == 0:
                state[0] , state[1], state[2] = state[0] + num, state[1] + num if state[1] else 0, state[2] + num if state[2] else 0
            if num % 3 == 1:
                state[0], state[1], state[2] = max(state[2] + num if state[2] else 0, state[0]), max(state[0] + num, state[1]), max(state[1] + num if state[1] else 0, state[2])
            if num % 3 == 2:
                state[0], state[1], state[2] = max(state[1] + num if state[1] else 0, state[0]), max(state[2] + num if state[2] else 0, state[1]), max(state[0] + num, state[2])
        return state[0]

class Solution1(object):

    def get_min_2_sum(self, nums):
        min_2_sum = 0
        min_2_sum += min(nums)
        nums.remove(min_2_sum)
        min_2_sum += min(nums)
        return min_2_sum
        

    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = sum(nums)
        nums_mod = sum_nums % 3
        if nums_mod == 0:
            return sum_nums
        mod_one = [num for num in nums if num % 3 == 1]
        mod_two = [num for num in nums if num % 3 == 2]
        min_one = min_two = 10001
        if nums_mod == 1:
            if mod_one:
                min_one = min(mod_one)
            if len(mod_two) > 1:
                min_two = self.get_min_2_sum(mod_two) 
        if nums_mod == 2:
            if mod_two:
                min_two = min(mod_two)
            if len(mod_one) > 1:
                min_one = self.get_min_2_sum(mod_one)
        return sum_nums - min(min_one, min_two)

# @lc code=end

