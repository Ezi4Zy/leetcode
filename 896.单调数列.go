/*
 * @lc app=leetcode.cn id=896 lang=golang
 *
 * [896] 单调数列
 */
package main

// @lc code=start
func isMonotonic(nums []int) bool {
	status := -1
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			if nums[i] > nums[i-1] {
				if status == 0 {
					return false
				}
				status = 1
			} else {
				if status == 1 {
					return false
				}
				status = 0
			}
		}
	}
	return true
}

// func main() {
// fmt.Println(isMonotonic([]int{1, 2, 2, 3}), isMonotonic([]int{6, 5, 4, 4}), isMonotonic([]int{1, 3, 2}))
// }

// @lc code=end
