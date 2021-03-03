#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start

def cmp(interval1, interval2):
    if interval1[0] > interval2[0]:
        return 1
    elif interval1[0] == interval2[0]:
        return 0
    else:
        return -1
    

class Solution(object):
    
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(cmp)
        ret = []
        for interval in intervals:
            last_interval = ret[-1] if ret else []
            if last_interval and last_interval[-1] >= interval[0]:
                ret[-1][-1] = max(last_interval[1], interval[1])
            else:
                ret.append(interval)
        return ret
# @lc code=end

