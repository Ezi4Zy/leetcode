/*
 * @lc app=leetcode.cn id=1752 lang=golang
 *
 * [1752] 检查数组是否经排序和轮转得到
 */

// @lc code=start

package main

func check(nums []int) bool {
	flag := false
	pre := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] < nums[i-1] {
			if !flag {
				flag = true
			} else {
				return false
			}
		}
		if flag && nums[i] > pre {
			return false
		}
	}
	return true
}

// func main() {
// fmt.Println(check([]int{3, 4, 5, 1, 2}))
// fmt.Println(check([]int{2, 1, 3, 4}))
// fmt.Println(check([]int{1, 2, 3}))
// fmt.Println(check([]int{1, 1, 1}))
// fmt.Println(check([]int{1, 2}))
// }

// @lc code=end
