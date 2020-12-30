#
# @lc app=leetcode.cn id=401 lang=python
#
# [401] 二进制手表
#

# @lc code=start

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        hour_bit_count_map = [[0], [1, 2, 4, 8], [3, 5, 6, 9, 10], [7, 11]]
        minute_bit_count_map = [
            [0], 
            [1, 2, 4, 8, 16, 32], 
            [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48], 
            [7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44, 49, 50, 52, 56], 
            [15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58], 
            [31, 47, 55, 59]
        ]
        for hour_bit_count in range(4):
            minute_bit_count = num - hour_bit_count
            if minute_bit_count > 5 or minute_bit_count < 0:
                continue
            else:
                for hour in hour_bit_count_map[hour_bit_count]:
                    for minute in minute_bit_count_map[minute_bit_count]:
                        ret.append(str(hour) + ":" + (('0' + str(minute)) if minute < 10 else str(minute)))
        return ret

class Solution1(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        hour_bit_count_map = [[], [], [], []]
        for hour in range(12):
            count = 0
            tmp = hour
            while tmp:
                count += tmp % 2
                tmp /= 2
            hour_bit_count_map[count].append(hour)
        minute_bit_count_map = [[], [], [], [], [], []]
        for minute in range(60):
            count = 0
            tmp = minute
            while tmp:
                count += tmp % 2
                tmp /= 2
            minute_bit_count_map[count].append(minute)
        print hour_bit_count_map, minute_bit_count_map
        for hour_bit_count in range(4):
            minute_bit_count = num - hour_bit_count
            if minute_bit_count > 5 or minute_bit_count < 0:
                continue
            else:
                for hour in hour_bit_count_map[hour_bit_count]:
                    for minute in minute_bit_count_map[minute_bit_count]:
                        ret.append(str(hour) + ":" + (('0' + str(minute)) if minute < 10 else str(minute)))
        return ret

# @lc code=end

