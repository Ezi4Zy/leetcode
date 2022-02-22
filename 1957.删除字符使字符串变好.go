/*
 * @lc app=leetcode.cn id=1957 lang=golang
 *
 * [1957] 删除字符使字符串变好
 */
package main

// @lc code=start
func makeFancyString(s string) string {
	ret := make([]byte, len(s))
	index := 0
	for i := 0; i < len(s); i++ {
		if i < 2 || s[i] != ret[index-1] || s[i] != ret[index-2] {
			ret[index] = s[i]
			index++
		}
	}
	return string(ret[:index])
}

// func main() {
// fmt.Println(makeFancyString("leeetcode"))
// fmt.Println(makeFancyString("aaabaaaa"))
// fmt.Println(makeFancyString("aab"))
// }

// @lc code=end
