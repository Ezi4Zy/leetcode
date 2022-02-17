/*
 * @lc app=leetcode.cn id=1047 lang=golang
 *
 * [1047] 删除字符串中的所有相邻重复项
 */
package main

// @lc code=start
func removeDuplicates(s string) string {
	ret := make([]byte, len(s))
	index := -1
	for i := 0; i < len(s); i++ {
		if index >= 0 && s[i] == ret[index] {
			index--
		} else {
			index++
			ret[index] = s[i]
		}
	}
	return string(ret[:index+1])
}

// func main() {
// fmt.Println(removeDuplicates("abbaca"), removeDuplicates("a"), removeDuplicates("aa"))
// }

// @lc code=end
