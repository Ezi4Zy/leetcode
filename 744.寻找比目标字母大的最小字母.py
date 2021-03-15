#
# @lc app=leetcode.cn id=744 lang=python
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters = list(set(letters))
        letters.sort()
        start = 0
        end = len(letters) - 1
        while end > start:
            mid = (start + end) / 2
            if letters[mid] > target:
                end = mid
            else:
                start = mid + 1
        if letters[start] > target:
            return letters[start]
        else:
            return letters[(start+1) % len(letters)]
# @lc code=end

