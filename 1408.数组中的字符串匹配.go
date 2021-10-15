/*
 * @lc app=leetcode.cn id=1408 lang=golang
 *
 * [1408] 数组中的字符串匹配
 */

// @lc code=start
package main

import (
	"sort"
	"strings"
)

func stringMatching(words []string) []string {
	ret := []string{}
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	for i := 0; i < len(words); i++ {
		for j := i + 1; j < len(words); j++ {
			if strings.Contains(words[j], words[i]) {
				ret = append(ret, words[i])
				break
			}
		}
	}
	return ret
}

// @lc code=end
