/*
 * @lc app=leetcode.cn id=1935 lang=golang
 *
 * [1935] 可以输入的最大单词数
 */
package main

// @lc code=start
func canBeTypedWords(text string, brokenLetters string) int {
	brokenLettersMap := make(map[byte]bool, len(brokenLetters))
	for i := 0; i < len(brokenLetters); i++ {
		brokenLettersMap[brokenLetters[i]] = true
	}
	index := 0
	count := 0
	flag := true
	for index <= len(text) {
		if index == len(text) || text[index] == ' ' {
			if flag {
				count++
			}
			flag = true
		} else {
			if brokenLettersMap[text[index]] {
				flag = false
			}
		}
		index++
	}
	return count
}

// func main() {
// fmt.Println(canBeTypedWords("hello world", "ad"), canBeTypedWords("leet code", "lt"), canBeTypedWords("leet code", "e"))
// }

// @lc code=end
