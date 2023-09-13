/*
 * @lc app=leetcode.cn id=2042 lang=golang
 *
 * [2042] 检查句子中的数字是否递增
 */

package main

import (
	"fmt"
)

// @lc code=start
func areNumbersAscending(s string) bool {
	pre := 0
	index := 0
	for index < len(s) {
		if s[index] > '0' && s[index] <= '9' {
			num := 0
			for index != len(s) && s[index] != ' ' {
				num = num*10 + int(s[index]-'0')
				index++
			}
			if num <= pre {
				return false
			}
			pre = num
		}
		index++
	}
	return true
}

// @lc code=end

func main() {
	fmt.Println(areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
	fmt.Println(areNumbersAscending("hello world 5 x 5"))
	fmt.Println(areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))
}
