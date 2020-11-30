#
# @lc app=leetcode.cn id=1504 lang=python
#
# [1504] 统计全 1 子矩形
#

1 0 1
1 1 0
1 1 0

1 0 1
1 2 0
1 2 0

# @lc code=start
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ret = 0
        left = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j-1] + 1
        print left
        for i in range(len(left)):
            for j in range(len(left[0])):
                min_ = left[i][j]
                k = i
                while k >= 0 and min_:
                    min_ = min(left[k][j], min_)
                    ret += min_
                    k -= 1
        return ret
                
# @lc code=end

