/*
 * @lc app=leetcode.cn id=1974 lang=golang
 *
 * [1974] 使用特殊打字机键入单词的最少时间
 */

package main

import "fmt"

// @lc code=start
func minTimeToType(word string) int {
	count := 0
	pre := 'a'
	for _, c := range word {
		steps := int(c - pre)
		if steps < 0 {
			steps = -steps
		}
		if steps > 13 {
			steps = 26 - steps
		}
		count += steps + 1
		pre = c
	}
	return count
}

// @lc code=end

func main() {
	fmt.Println(minTimeToType("abc"))
	fmt.Println(minTimeToType("bza"))
	fmt.Println(minTimeToType("zjpc"))
}
