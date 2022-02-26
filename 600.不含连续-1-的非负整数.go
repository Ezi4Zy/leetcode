/*
 * @lc app=leetcode.cn id=600 lang=golang
 *
 * [600] 不含连续1的非负整数
 */
package main

// @lc code=start
func find(max, cur int) int {
	count := 0
	if cur*2 <= max {
		count++
		count += find(max, cur*2)
	}
	if cur*2+1 <= max && cur%2 == 0 {
		count++
		count += find(max, cur*2+1)
	}
	return count
}
func findIntegers(n int) int {
	count := 2
	count += find(n, 1)

	return count
}

// func main() {
// fmt.Println(findIntegers(5))
// fmt.Println(findIntegers(1))
// fmt.Println(findIntegers(1000000000))
// }

// @lc code=end
