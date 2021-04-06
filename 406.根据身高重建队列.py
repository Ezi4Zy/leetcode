#
# @lc app=leetcode.cn id=406 lang=python
# 
# 根据身高重建队列
# 

# @lc code=start
class Solution(object):
    
    
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def cmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return b[1] - a[1]
        people.sort(cmp=cmp, reverse=True)
        ret = []
        for p in people:
            h, k = p[0], p[1]
            if k == 0:
                ret = [p] + ret
            else:
                for index in range(len(ret)):
                    if h <= ret[index][0]:
                        k -= 1
                        if k == 0:
                            break
                ret = ret[:index+1] + [p] + ret[index+1:]
        return ret
# @lc code=end

