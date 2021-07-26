/*
 * @lc app=leetcode.cn id=1827 lang=golang
 *
 * [1827] 最少操作使数组递增
 */

// @lc code=start
// package main
//
// import "fmt"

func minOperations(nums []int) int {
	ret := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] <= nums[i-1] {
			ret += nums[i-1] - nums[i] + 1
			nums[i] = nums[i-1] + 1
		}
	}
	return ret

}

// func main() {
// fmt.Println(minOperations([]int{1, 1, 1}))
// fmt.Println(minOperations([]int{1, 5, 2, 4, 1}))
// }

// @lc code=end
