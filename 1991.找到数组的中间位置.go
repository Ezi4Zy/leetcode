/*
 * @lc app=leetcode.cn id=1991 lang=golang
 *
 * [1991] 找到数组的中间位置
 */

package main

import "fmt"

// @lc code=start
func findMiddleIndex(nums []int) int {
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
	}
	left := 0
	for i := 0; i < len(nums); i++ {
		if sum-nums[i] == left*2 {
			return i
		}
		left += nums[i]
	}
	return -1
}

// @lc code=end

func main() {
	fmt.Println(findMiddleIndex([]int{2, 3, -1, 8, 4}))
	fmt.Println(findMiddleIndex([]int{1, -1, 4}))
	fmt.Println(findMiddleIndex([]int{2, 5}))
	fmt.Println(findMiddleIndex([]int{1}))

}
