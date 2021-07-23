/*
 * @lc app=leetcode.cn id=1920 lang=golang
 *
 * [1920] 基于排列构建数组
 */

// @lc code=start
// package leetcode

func buildArray(nums []int) []int {
	ans := []int{}
	for i := 0; i < len(nums); i++ {
		ans = append(ans, nums[nums[i]])

	}
	return ans
}

// @lc code=end
