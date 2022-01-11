/*
 * @lc app=leetcode.cn id=1342 lang=golang
 *
 * [1342] 将数字变成 0 的操作次数
 */
package main

// @lc code=start
func numberOfSteps(num int) int {
	count := 0
	for num > 1 {
		count += 1 + num%2
		num /= 2
	}
	return count + num
}

// func main() {
// fmt.Print(numberOfSteps(14))
// fmt.Print(numberOfSteps(8))
// fmt.Print(numberOfSteps(123))
// }

// @lc code=end
