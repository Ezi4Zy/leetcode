/*
 * @lc app=leetcode.cn id=1528 lang=golang
 *
 * [1528] 重新排列字符串
 */

// @lc code=start
package main

func restoreString(s string, indices []int) string {
	b := make([]byte, len(s))
	for i := 0; i < len(indices); i++ {
		b[indices[i]] = s[i]
	}
	return string(b)
}

// func main() {
// fmt.Println(restoreString("codeleet", []int{4, 5, 6, 7, 0, 2, 1, 3}))
// }

// @lc code=end
