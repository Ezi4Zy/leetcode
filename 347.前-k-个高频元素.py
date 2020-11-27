#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
from heapq import * 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.Counter()
        for num in nums:
            dic[num] += 1
        l = []
        for num, count in dic.iteritems():
            if len(l) < k:
                heappush(l, (count, num))
            else:
                if l[0][0] < count:
                    heappop(l)
                    heappush(l, (count, num))
        return [i[1] for i in l]
            
# @lc code=end

