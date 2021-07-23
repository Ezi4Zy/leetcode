/*
 * @lc app=leetcode.cn id=1913 lang=golang
 *
 * [1913] 两个数对之间的最大乘积差
 */

// @lc code=start
// package leetcode

func maxProductDifference(nums []int) int {
	max1, max2 := 0, 0
	min1, min2 := 10001, 10001
	for i := 0; i < len(nums); i++ {
		if nums[i] > max2 {
			max2 = nums[i]
			if max2 > max1 {
				max1, max2 = max2, max1
			}
		}
		if nums[i] < min2 {
			min2 = nums[i]
			if min2 < min1 {
				min1, min2 = min2, min1
			}
		}
	}
	return max1*max2 - min1*min2

}

// @lc code=end
