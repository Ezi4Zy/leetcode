/*
 * @lc app=leetcode.cn id=453 lang=golang
 *
 * [453] 最小操作次数使数组元素相等
 */

// @lc code=start

func minMoves(nums []int) int {
	ret := 0
	if len(nums) > 0 {
		min_num := nums[0]
		for _, num := range nums {
			if min_num > num {
				min_num = num
			}
		}
		for _, num := range nums {
			ret += num - min_num
		}
	}
	return ret
}

// @lc code=end

