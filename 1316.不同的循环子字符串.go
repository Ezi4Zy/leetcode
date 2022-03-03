/*
 * @lc app=leetcode.cn id=1316 lang=golang
 *
 * [1316] 不同的循环子字符串
 */
package main

// @lc code=start
func distinctEchoSubstrings(text string) int {
	count := 0
	indexes := make([][]int, 26)
	for i := 0; i < len(text); i++ {
		indexes[text[i]-'a'] = append(indexes[text[i]-'a'], i)
	}
	for i := 0; i < len(indexes); i++ {
		letterIndexes := indexes[i]
		letterMap := make(map[string]bool)
		for m := 0; m < len(letterIndexes); m++ {
			start := letterIndexes[m]
			for n := m + 1; n < len(letterIndexes); n++ {
				end := letterIndexes[n]
				if !letterMap[text[start:end]] && len(text)-end >= end-start && text[start:end] == text[end:2*end-start] {
					letterMap[text[start:end]] = true
					count++
				}
			}
		}
	}
	return count
}

// func main() {
// fmt.Println(distinctEchoSubstrings("abcabcabc"))
// fmt.Println(distinctEchoSubstrings("leetcodeleetcode"))
// }

// @lc code=end
