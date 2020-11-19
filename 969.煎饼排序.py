#
# @lc app=leetcode.cn id=969 lang=python
#
# [969] 煎饼排序
#
[3,2,4,1]
[4,2,3,1] 3
[1,3,2,4] 4
[3,1,2,4] 2
[]

[a,b,c,d,e,f]
d
[d,c,b,a,e,f]
[f,e,a,b,c,d]

# @lc code=start

class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ret = []
        end = len(arr)
        sorted_arr = sorted(arr)
        while end > 1:
            index = arr.index(sorted_arr[end-1])
            if index:
                if index != end-1:
                    arr = arr[index+1:end][::-1] + arr[:index]
                    ret.extend([index+1, end])
            else:
                arr = arr[:end][::-1]
                ret.append(end)
            end -= 1
        return ret

class Solution1(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ret = []
        end = len(arr)
        while end:
            index = arr.index(max(arr[:end]))
            if index != end-1:
                if index != 0:
                    ret.append(index+1)
                    mid = index / 2
                    if index % 2:
                        m = mid
                        n = mid + 1
                    else:
                        m = mid - 1
                        n = mid + 1
                    while m >= 0:
                        arr[m], arr[n] = arr[n], arr[m]
                        m -= 1
                        n += 1
                ret.append(end)
                mid = (end-1) / 2
                if (end-1) % 2:
                    m = mid
                    n = mid + 1
                else:
                    m = mid - 1
                    n = mid + 1
                while m >= 0:
                    arr[m], arr[n] = arr[n], arr[m]
                    m -= 1
                    n += 1
            end -= 1
        return ret
# @lc code=end

