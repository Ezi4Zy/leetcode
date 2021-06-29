#
# @lc app=leetcode.cn id=1481 lang=python
#
# [1481] 不同整数的最少数目
#

# @lc code=start
import collections
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        val_count = collections.Counter()
        for i in arr:
            val_count[i] += 1
        ret = len(val_count.keys())
        for val in sorted(val_count.keys(), key=lambda x: val_count[x]):
            if val_count[val] <= k:
                k -= val_count[val]
                ret -= 1
            else:
                break
        return ret

        
# @lc code=end

