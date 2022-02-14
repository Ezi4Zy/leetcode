/*
 * @lc app=leetcode.cn id=884 lang=golang
 *
 * [884] 两句话中的不常见单词
 */
package main

// @lc code=start
func uncommonFromSentences(s1 string, s2 string) []string {
	wordCount := make(map[string]int)
	start := 0
	for i := 1; i < len(s1); {
		for i < len(s1) && s1[i] != ' ' {
			i++
		}
		wordCount[s1[start:i]]++
		start = i + 1
		i++
	}
	start = 0
	for i := 1; i < len(s2); {
		for i < len(s2) && s2[i] != ' ' {
			i++
		}
		wordCount[s2[start:i]]++
		start = i + 1
		i++
	}
	ret := []string{}
	for word, count := range wordCount {
		if count == 1 {
			ret = append(ret, word)
		}
	}
	return ret
}

// func main() {
// fmt.Println(uncommonFromSentences("this apple is sweet", "this apple is sour"),
// uncommonFromSentences("apple apple", "banana"))
// }

// @lc code=end
