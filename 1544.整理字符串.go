/*
 * @lc app=leetcode.cn id=1544 lang=golang
 *
 * [1544] 整理字符串
 */

// @lc code=start
package main

func makeGood(s string) string {
	length := len(s)
	r := make([]byte, length)
	index := 0
	constDiff := 'A' - 'a'
	for i := 0; i < length; i++ {
		if index > 0 {
			if s[i]-r[index-1] == byte(constDiff) || r[index-1]-s[i] == byte(constDiff) {
				index--
			} else {
				r[index] = s[i]
				index++
			}
		} else {
			r[index] = s[i]
			index++
		}
	}
	return string(r[:index])

}

//
// func main() {
// fmt.Println(makeGood("leEeetcode"), makeGood("abBAcC"), makeGood("s"))
// }
//
// @lc code=end
