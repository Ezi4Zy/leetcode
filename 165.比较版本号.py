#
# @lc app=leetcode.cn id=165 lang=python
#
# [165] 比较版本号
#

# @lc code=start
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        for i in range(max(len(version1), len(version2))):
            if i < len(version1):
                current_version1 = int(version1[i])
            else:
                current_version1 = 0
            if i < len(version2):
                current_version2 = int(version2[i])
            else:
                current_version2 = 0
            if current_version1 > current_version2:
                return 1
            elif current_version1 < current_version2:
                return -1
            else:
                continue
        else:
            return 0
# @lc code=end

