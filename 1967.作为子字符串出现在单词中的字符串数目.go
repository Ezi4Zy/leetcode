/*
 * @lc app=leetcode.cn id=1967 lang=golang
 *
 * [1967] 作为子字符串出现在单词中的字符串数目
 */

package main

// @lc code=start
func numOfStrings(patterns []string, word string) int {
	count := 0
	counter := make(map[string]struct{}, 0)
	for _, pattern := range patterns {
		for i := 0; i <= len(word)-len(pattern); i++ {
			if _, ok := counter[pattern]; ok {
				count++
				break
			}
			if pattern == word[i:i+len(pattern)] {
				counter[pattern] = struct{}{}
				count++
				break
			}
		}
	}
	return count
}

// func main() {
// fmt.Println(numOfStrings(
// []string{"a", "abc", "bc", "d"},
// "abc"))
// fmt.Println(numOfStrings(
// []string{"a", "b", "c"},
// "aaaaabbbbb"))
// fmt.Println(numOfStrings(
// []string{"a", "a", "a"},
// "abc"))
// }

// @lc code=end
