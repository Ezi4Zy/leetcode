#
# @lc app=leetcode.cn id=48 lang=python
# 
# 旋转图像
# 

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            start = i
            end = n - 1 - i
            if end > start:
                for j in range(start, end):
                    diff = j - i
                    matrix[i][j], matrix[j][end], matrix[end][end-diff], matrix[end-diff][i] = matrix[end-diff][i], matrix[i][j], matrix[j][end], matrix[end][end-diff]
        return matrix


# @lc code=end

