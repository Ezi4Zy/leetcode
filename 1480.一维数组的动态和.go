/*
 * @lc app=leetcode.cn id=1480 lang=golang
 *
 * [1480] 一维数组的动态和
 */

// @lc code=start
package main

func runningSum(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	return nums

}

//
// func main() {
// fmt.Println(runningSum([]int{1, 2, 3, 4}))
// fmt.Println(runningSum([]int{1, 1, 1, 1, 1}))
// fmt.Println(runningSum([]int{3, 1, 2, 10, 1}))
// }

// @lc code=end
