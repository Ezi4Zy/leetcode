/*
 * @lc app=leetcode.cn id=1848 lang=golang
 *
 * [1848] 到目标元素的最小距离
 */

// @lc code=start
// package main
//
// import "fmt"

func getMinDistance(nums []int, target int, start int) int {
	length := len(nums)
	var left, right int
	if length > start {
		left = start
		right = start
	} else {
		left = length - 1
		right = length - 1
	}
	for {
		if left >= 0 {
			if nums[left] == target {
				return start - left
			}
			left--
		}
		if right < length {
			if nums[right] == target {
				return right - start
			}
			right++
		}
	}
}

// func main() {
// fmt.Println(getMinDistance([]int{1, 2, 3, 4, 5}, 5, 3))
// }

// @lc code=end
