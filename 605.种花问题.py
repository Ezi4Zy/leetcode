#
# @lc app=leetcode.cn id=605 lang=python
#
# [605] 种花问题
#

# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        for index in range(1, len(flowerbed)-1):
            if not (flowerbed[index-1] or flowerbed[index] or flowerbed[index+1]):
                flowerbed[index] = 1
                n -= 1
        return n <= 0
        
        
        
class Solution1(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        flag = True
        ret = 0
        count = 0
        for index in range(len(flowerbed)):
            if flag:
                if flowerbed[index] == 0:
                    count += 1
                else:
                    ret += (count - 1) / 2
                    flag = False
                    count = 0
            else:
                if flowerbed[index] == 0:
                    flag = True
                    count += 1
        else:
            ret += (count - 1) / 2
        return ret >= n
# @lc code=end

