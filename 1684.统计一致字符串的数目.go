/*
 * @lc app=leetcode.cn id=1684 lang=golang
 *
 * [1684] 统计一致字符串的数目
 */

// @lc code=start
package main

func countConsistentStrings(allowed string, words []string) int {
	byteList := make([]bool, 26)
	count := 0
	for i := 0; i < len(allowed); i++ {
		byteList[allowed[i]-'a'] = true
	}
	for _, word := range words {
		flag := true
		for i := 0; i < len(word); i++ {
			if !byteList[word[i]-'a'] {
				flag = false
				break
			}
		}
		if flag {
			count++
		}
	}
	return count
}

// func main() {
// fmt.Println(countConsistentStrings("abc", []string{"a", "b", "c", "ab", "ac", "bc", "abc"}))
// }

// @lc code=end
