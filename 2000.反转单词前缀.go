/*
 * @lc app=leetcode.cn id=2000 lang=golang
 *
 * [2000] 反转单词前缀
 */

package main

import (
	"fmt"
	"strings"
)

// @lc code=start
func reversePrefix(word string, ch byte) string {
	right := strings.IndexByte(word, ch)
	if right == -1 {
		return word
	}
	newWord := []byte(word)
	left := 0
	for left < right {
		newWord[left], newWord[right] = newWord[right], newWord[left]
		left++
		right--
	}
	return string(newWord)
}

// @lc code=end

func main() {
	fmt.Println(reversePrefix("abcdefg", 'd'))
	fmt.Println(reversePrefix("xyxzxe", 'z'))
	fmt.Println(reversePrefix("abcd", 'z'))
}
