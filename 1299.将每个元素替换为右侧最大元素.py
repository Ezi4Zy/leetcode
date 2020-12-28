#
# @lc app=leetcode.cn id=1299 lang=python
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_num = arr[0]
        for index, num in enumerate(arr):
            if index == len(arr) - 1:
                arr[index] = -1
            else:
                if arr[index] == max_num:
                    max_num = max(arr[index+1:])
                arr[index] = max_num
        return arr
    
# @lc code=end

