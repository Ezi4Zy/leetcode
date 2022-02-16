/*
 * @lc app=leetcode.cn id=1002 lang=golang
 *
 * [1002] 查找共用字符
 */
package main

import (
	"sort"
	"strings"
)

// @lc code=start
func commonChars(words []string) []string {
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	counter := map[string]int{}
	for i := 0; i < len(words[0]); i++ {
		tmp := words[0][i : i+1]
		flag := true
		for j := 1; j < len(words); j++ {
			if strings.Count(words[j], tmp) < counter[tmp]+1 {
				flag = false
				break
			}
		}
		if flag {
			counter[tmp]++
		}
	}
	ret := []string{}
	for s, count := range counter {
		for count > 0 {
			ret = append(ret, s)
			count--
		}
	}
	return ret
}

// func main() {
// fmt.Println(commonChars([]string{"bella", "label", "roller"}), commonChars([]string{"cool", "lock", "cook"}))
// }

// @lc code=end
