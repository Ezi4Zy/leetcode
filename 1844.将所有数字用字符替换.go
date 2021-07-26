/*
 * @lc app=leetcode.cn id=1844 lang=golang
 *
 * [1844] 将所有数字用字符替换
 */

// @lc code=start
// package main

func shift(b byte, d byte) byte {
	return byte(b + d - '0')
}
func replaceDigits(s string) string {
	b := []byte(s)
	pre := b[0]
	for i := 1; i < len(b); i++ {
		if i%2 == 1 {
			b[i] = shift(pre, b[i])
		} else {
			pre = b[i]
		}
	}
	return string(b)

}

// func main() {
// fmt.Println(replaceDigits("a1c1e1"))
// }

// @lc code=end
