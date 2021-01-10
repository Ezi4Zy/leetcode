#
# @lc app=leetcode.cn id=599 lang=python
#
# [599] 两个列表的最小索引总和
#

# @lc code=start

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        same_restaurant = set(list1) & set(list2)
        dic = {}
        for restaurant in same_restaurant:
            dic.setdefault(list1.index(restaurant) + list2.index(restaurant), []).append(restaurant)
        return dic[min(dic.keys())]

class Solution1(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        for total_index in range(len(list1) + len(list2) - 1):
            ret = []
            for list1_index in range(min(total_index + 1, len(list1))):
                list2_index = total_index - list1_index
                if 0 <= list2_index < len(list2):
                    if list1[list1_index] == list2[list2_index]:
                        ret.append(list1[list1_index])
            if ret:
                return ret
# @lc code=end

