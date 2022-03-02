/*
 * @lc app=leetcode.cn id=2124 lang=golang
 *
 * [2124] 检查是否所有 A 都在 B 之前
 */
package main

// @lc code=start
func checkString(s string) bool {
	b := false
	for i := 0; i < len(s); i++ {
		if s[i] == 'a' {
			if b {
				return false
			}
		} else {
			b = true
		}
	}
	return true
}

// func main() {
// fmt.Println(checkString("aaabbb"))
// fmt.Println(checkString("abab"))
// fmt.Println(checkString("bbb"))
// }

// @lc code=end
