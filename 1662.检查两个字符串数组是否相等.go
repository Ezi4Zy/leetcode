/*
 * @lc app=leetcode.cn id=1662 lang=golang
 *
 * [1662] 检查两个字符串数组是否相等
 */

// @lc code=start
package main

func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	i1 := 0
	j1 := 0
	i2 := 0
	j2 := 0
	for i1 < len(word1) && i2 < len(word2) {
		if word1[i1][j1] != word2[i2][j2] {
			return false
		}
		if j1 == len(word1[i1])-1 {
			i1++
			j1 = 0
		} else {
			j1++
		}
		if j2 == len(word2[i2])-1 {
			i2++
			j2 = 0
		} else {
			j2++
		}
	}
	if i1 == len(word1) && j1 == 0 && i2 == len(word2) && j2 == 0 {
		return true
	}
	return false
}

//
// func main() {
// fmt.Println(arrayStringsAreEqual([]string{"ab", "c"}, []string{"a", "bc"}))
// }

// @lc code=end
