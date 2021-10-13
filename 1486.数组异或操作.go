/*
 * @lc app=leetcode.cn id=1486 lang=golang
 *
 * [1486] 数组异或操作
 */

// @lc code=start
package main

func xorOperation(n int, start int) int {
	ret := start
	for i := 1; i < n; i++ {
		ret ^= start + i*2
	}
	return ret
}

//
// func main() {
// fmt.Println(xorOperation(5, 0))
// fmt.Println(xorOperation(4, 3))
// fmt.Println(xorOperation(1, 7))
// }

// @lc code=end
