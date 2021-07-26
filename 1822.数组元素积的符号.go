/*
 * @lc app=leetcode.cn id=1822 lang=golang
 *
 * [1822] 数组元素积的符号
 */

// @lc code=start
// package main

func arraySign(nums []int) int {
	ret := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			return 0
		}
		if nums[i] < 0 {
			ret++
		}
	}
	if ret%2 == 1 {
		return -1
	} else {
		return 1
	}
}

// func main() {
// fmt.Println(arraySign([]int{-1, -2, -3, -4, 3, 2, 1, 0}))
// fmt.Println(arraySign([]int{-1, -2, -3, -4, 3, 2, 1}))
// fmt.Println(arraySign([]int{-2, -3, -4, 3, 2, 1}))
// }

// @lc code=end
