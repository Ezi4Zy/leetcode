/*
 * @lc app=leetcode.cn id=1137 lang=golang
 *
 * [1137] 第 N 个泰波那契数
 */
package main

// @lc code=start
var TriList = [38]int{
	0,
	1,
	1,
}

func tribonacci(n int) int {
	if n != 0 && TriList[n] == 0 {
		TriList[n] = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
	}
	return TriList[n]
}

// func main() {
// fmt.Println(tribonacci(4), tribonacci(25))
// }

// @lc code=end
