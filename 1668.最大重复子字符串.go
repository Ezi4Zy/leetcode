/*
 * @lc app=leetcode.cn id=1668 lang=golang
 *
 * [1668] 最大重复子字符串
 */

// @lc code=start
package main

import (
	"strings"
)

func maxRepeating(sequence string, word string) int {
	for i := 0; i < len(sequence); i++ {
		if strings.Index(sequence, strings.Repeat(word, i+1)) == -1 {
			return i
		}
	}
	return len(sequence) / len(word)
}

// func main() {
// fmt.Println(maxRepeating("ababc", "ab"))
// }

// @lc code=end
