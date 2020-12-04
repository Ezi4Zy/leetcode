#
# @lc app=leetcode.cn id=992 lang=python
#
# [992] K 个不同整数的子数组
#

# @lc code=start
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        counter1 = collections.Counter()
        counter2 = collections.Counter()
        left1 = 0
        left2 = 0
        ans = 0
        for right, x in enumerate(A):
            counter1[x] += 1
            counter2[x] += 1
            
            while len(counter1.keys()) > K:
                counter1[A[left1]] -= 1
                if counter1[A[left1]] == 0:
                    counter1.pop(A[left1])
                left1 +=1
            
            while len(counter2.keys()) >= K:
                counter2[A[left2]] -= 1
                if counter2[A[left2]] == 0:
                    counter2.pop(A[left2])
                left2 +=1
            ans += left2 - left1
        return ans
 
# @lc code=end

