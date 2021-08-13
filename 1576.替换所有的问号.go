/*
 * @lc app=leetcode.cn id=1576 lang=golang
 *
 * [1576] 替换所有的问号
 */

// @lc code=start
package main

func modifyString(s string) string {
	b := []byte(s)
	chars := "abcdefghijklmnopqrstuvwxyz"
	for i := 0; i < len(b); i++ {
		if b[i] == '?' {
			for j := 0; j < len(chars); j++ {
				if (i == 0 || b[i-1] != chars[j]) && (i == len(b)-1 || b[i+1] != chars[j]) {
					b[i] = chars[j]
					break
				}
			}
		}
	}
	return string(b)
}

//
// func main() {
// fmt.Println(modifyString("???zs???"))
// }

// @lc code=end
