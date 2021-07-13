/*
 * @lc app=leetcode.cn id=791 lang=golang
 *
 * [791] 自定义字符串排序
 */

// @lc code=start
// package leetcode

import "sort"

var priority = make(map[rune]int)

type byPriority []rune

func (t byPriority) Len() int {
	return len(t)
}

func (t byPriority) Swap(i, j int) {
	t[i], t[j] = t[j], t[i]
}

func (t byPriority) Less(i, j int) bool {
	return priority[t[i]] > priority[t[j]]
}

func customSortString(order string, str string) string {
	for index, c := range order {
		priority[c] = -index
	}
	r := []rune(str)
	sort.Sort(byPriority(r))
	return string(r)
}

// @lc code=end

