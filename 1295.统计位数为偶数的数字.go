/*
 * @lc app=leetcode.cn id=1295 lang=golang
 *
 * [1295] 统计位数为偶数的数字
 */
package main

// @lc code=start
func findNumbers(nums []int) int {
	count := 0
	for i := 0; i < len(nums); i++ {
		numCount := 1
		for nums[i] > 9 {
			numCount++
			nums[i] /= 10
		}
		if numCount%2 == 0 {
			count++
		}
	}
	return count
}

// func main() {
// fmt.Println(findNumbers([]int{12, 345, 2, 6, 7896}))
// fmt.Println(findNumbers([]int{555, 901, 482, 1771}))
// }

// @lc code=end
