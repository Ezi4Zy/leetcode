/*
 * @lc app=leetcode.cn id=334 lang=golang
 *
 * [334] 递增的三元子序列
 */

// @lc code=start
// package leetcode

func increasingTriplet(nums []int) bool {
	min1 := nums[0]
	is_min2 := false
	var min2 int
	for i := 1; i < len(nums); i++ {
		if is_min2 {
			if nums[i] > min2 {
				return true
			} else {
				if nums[i] > min1 {
					min2 = nums[i]
				} else {
					min1 = nums[i]
				}
			}
		} else {
			if nums[i] <= min1 {
				min1 = nums[i]
			} else {
				min2 = nums[i]
				is_min2 = true
			}
		}
	}
	return false
}

// @lc code=end
