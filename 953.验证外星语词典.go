/*
 * @lc app=leetcode.cn id=953 lang=golang
 *
 * [953] 验证外星语词典
 */
package main

import (
	"sort"
	"strings"
)

// @lc code=start
func isAlienSorted(words []string, order string) bool {
	return sort.SliceIsSorted(words, func(i, j int) bool {
		index := 0
		for {
			if index < len(words[i]) && index < len(words[j]) {
				if words[i][index] != words[j][index] {
					return strings.Index(order, words[i][index:index+1]) < strings.Index(order, words[j][index:index+1])
				} else {
					index++
				}
			} else {
				return index == len(words[i]) && index != len(words[j])
			}
		}
	})
}

// func main() {
// fmt.Println(isAlienSorted([]string{"hello", "leetcode"}, "hlabcdefgijkmnopqrstuvwxyz"),
// isAlienSorted([]string{"word", "world", "row"}, "worldabcefghijkmnpqstuvxyz"),
// isAlienSorted([]string{"apple", "app"}, "abcdefghijklmnopqrstuvwxyz"),
// isAlienSorted([]string{"hello", "hello"}, "abcdefghijklmnopqrstuvwxyz"))
// }

// @lc code=end
