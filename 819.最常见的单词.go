/*
 * @lc app=leetcode.cn id=819 lang=golang
 *
 * [819] 最常见的单词
 */

// @lc code=start
package main

import (
	"strings"
)

func mostCommonWord(paragraph string, banned []string) string {
	bannedMap := make(map[string]bool, len(banned))
	counter := make(map[string]int)
	for _, b := range banned {
		bannedMap[b] = true
	}
	symbolMap := map[byte]bool{
		'?': true,
		'!': true,
		'.': true,
		',': true,
		' ': true,
		';': true,
		'\'': true,
	}
	for wordStart := 0; wordStart < len(paragraph); {
		if symbolMap[paragraph[wordStart]] {
			wordStart++
		} else {
			wordEnd := wordStart + 1
			for wordEnd < len(paragraph) {
				if !symbolMap[paragraph[wordEnd]] {
					wordEnd++
				} else {
					word := strings.ToLower(paragraph[wordStart:wordEnd])
					if !bannedMap[word] {
						counter[word]++
					}
					break
				}
			}
			if wordEnd == len(paragraph) {
				word := strings.ToLower(paragraph[wordStart:wordEnd])
				if !bannedMap[word] {
					counter[word]++
				}
			}
			wordStart = wordEnd
		}
	}
	mostCommonWord := ""
	mostCommonWordCount := 0
	for word, count := range counter {
		if count > mostCommonWordCount {
			mostCommonWord = word
			mostCommonWordCount = count
		}
	}
	return mostCommonWord
}

// func main() {
// fmt.Printf(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", []string{"hit"}))
// }

// @lc code=end
