#
# @lc app=leetcode.cn id=859 lang=python
#
# [859] 亲密字符串
#

# @lc code=start
class Solution(object):
    def buddyStrings(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        if len(a) != len(b):
            return False
        diff_count = 0
        diff_index = []
        for index in range(len(a)):
            if a[index] != b[index]:
                diff_count += 1
                diff_index.append(index)
        if diff_count == 0:
            return len(set(a)) != len(a)
        elif diff_count == 2:
            return a[diff_index[0]] == b[diff_index[1]] and a[diff_index[1]] == b[diff_index[0]]
        else:
            return False

       
# @lc code=end

