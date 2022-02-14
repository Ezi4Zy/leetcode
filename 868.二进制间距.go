/*
 * @lc app=leetcode.cn id=868 lang=golang
 *
 * [868] 二进制间距
 */
package main

// @lc code=start
func binaryGap(n int) int {
	ret := 0
	cur := -1
	for n > 0 {
		if n%2 == 1 {
			if cur >= 0 {
				cur++
				if cur > ret {
					ret = cur
				}
				cur = 0
			} else {
				cur = 0
			}
		} else {
			if cur >= 0 {
				cur++
			}
		}
		n /= 2
	}
	return ret
}

// func main() {
// fmt.Println(binaryGap(22), binaryGap(5), binaryGap(6), binaryGap(8), binaryGap(1))
// }

// @lc code=end
