#
# @lc app=leetcode.cn id=1535 lang=python
#
# [1535] 找出数组游戏的赢家
#
# @lc code=start

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(arr)
        pre = arr[0]
        win_count = 0
        for a in arr[1:]:
            if win_count == k:
                return pre
            if pre > a:
                win_count += 1
            else:
                pre = a
                win_count = 1
            if pre == max_num:
                return max_num
        

class Solution1(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(arr)-1:
            return max(arr)
        while True:
            i = 1
            while i < k + 1:
                if arr[0] < arr[i]:
                    arr = [arr[i],arr[0]] + arr[i+1:] + arr[1:i]
                    i = 1
                else:
                    i += 1
            return arr[0]  
# @lc code=end

