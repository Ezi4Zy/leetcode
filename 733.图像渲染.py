#
# @lc app=leetcode.cn id=733 lang=python
#
# [733] 图像渲染
#

# @lc code=start
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        oldColor, image[sr][sc] = image[sr][sc], newColor
        if sr - 1 >= 0 and oldColor == image[sr - 1][sc]:
            self.floodFill(image, sr - 1, sc, newColor)
        if sc - 1 >= 0 and oldColor == image[sr][sc - 1]:
            self.floodFill(image, sr, sc - 1, newColor)
        if sr + 1 < len(image) and  oldColor == image[sr + 1][sc]:
            self.floodFill(image, sr + 1, sc, newColor)
        if sc + 1 < len(image[0]) and oldColor == image[sr][sc + 1]:
            self.floodFill(image, sr, sc + 1, newColor)
        return image
# @lc code=end

