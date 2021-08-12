/*
 * @lc app=leetcode.cn id=1592 lang=golang
 *
 * [1592] 重新排列单词间的空格
 */

// @lc code=start
package main

import (
	"strings"
)

func reorderSpaces(text string) string {
	words := []string{}
	inWord := false
	wordStart := 0
	spaceCount := 0
	for i := 0; i < len(text); i++ {
		if text[i] != ' ' {
			if !inWord {
				inWord = true
				wordStart = i
			}
		} else {
			spaceCount++
			if inWord {
				inWord = false
				words = append(words, text[wordStart:i])
			}
		}
	}
	if inWord {
		words = append(words, text[wordStart:])
	}
	if len(words)-1 == 0 {
		return words[0] + strings.Repeat(" ", spaceCount)
	}
	tailSpaces := strings.Repeat(" ", spaceCount%(len(words)-1))
	return strings.Join(words, strings.Repeat(" ", spaceCount/(len(words)-1))) + tailSpaces
}

// func main() {
// fmt.Println(reorderSpaces("  this   is  a sentence "))
// fmt.Println(reorderSpaces(" practice   makes   perfect"))
// fmt.Println(reorderSpaces("  walks  udp package   into  bar a"))
// }

//
// @lc code=end
