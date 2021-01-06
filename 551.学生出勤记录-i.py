#
# @lc app=leetcode.cn id=551 lang=python
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = 0
        count_L = 0
        for c in s:
            if c == 'A':
                if count_A == 1:
                    return False
                count_A += 1
                count_L = 0
            elif c == 'L':
                if count_L == 2:
                    return False
                count_L += 1
            else:
                count_L = 0
        return True
        
# @lc code=end

