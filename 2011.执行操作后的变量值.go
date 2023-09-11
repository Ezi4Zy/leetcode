/*
 * @lc app=leetcode.cn id=2011 lang=golang
 *
 * [2011] 执行操作后的变量值
 */

package main

import "fmt"

// @lc code=start
func finalValueAfterOperations(operations []string) int {
	ret := 0
	for _, op := range operations {
		if op[1] == '+' {
			ret++
		} else {
			ret--
		}
	}
	return ret
}

// @lc code=end

func main() {
	fmt.Println(finalValueAfterOperations([]string{"--X", "X++", "X++"}))
	fmt.Println(finalValueAfterOperations([]string{"++X", "++X", "X++"}))
	fmt.Println(finalValueAfterOperations([]string{"X++", "++X", "--X", "X--"}))
}
