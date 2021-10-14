/*
 * @lc app=leetcode.cn id=1464 lang=golang
 *
 * [1464] 数组中两元素的最大乘积
 */

// @lc code=start
package main

func maxProduct(nums []int) int {
	top2 := make([]int, 2)
	for i := 0; i < len(nums); i++ {
		if nums[i] > top2[1] {
			if nums[i] > top2[0] {
				top2[0], top2[1] = nums[i], top2[0]
			} else {
				top2[1] = nums[i]
			}
		}
	}
	return (top2[0] - 1) * (top2[1] - 1)
}

//
// func main() {
// fmt.Println(maxProduct([]int{3, 4, 5, 2}))
// fmt.Println(maxProduct([]int{1, 5, 4, 5}))
// fmt.Println(maxProduct([]int{3, 7}))
// }

// @lc code=end
