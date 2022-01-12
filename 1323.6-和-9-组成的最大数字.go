/*
 * @lc app=leetcode.cn id=1323 lang=golang
 *
 * [1323] 6 和 9 组成的最大数字
 */
package main

// @lc code=start
func maximum69Number(num int) int {
	divider := 1000
	for divider > 0 {
		if num/divider%10 == 6 {
			return num + 3*divider
		}
		divider /= 10
	}
	return num
}

// func main() {
// fmt.Println(maximum69Number(9669))
// fmt.Println(maximum69Number(9996))
// fmt.Println(maximum69Number(9999))
// }

// @lc code=end
