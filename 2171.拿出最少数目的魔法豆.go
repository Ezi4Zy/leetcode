/*
 * @lc app=leetcode.cn id=2171 lang=golang
 *
 * [2171] 拿出最少数目的魔法豆
 */

package main

import (
	"sort"
)

// @lc code=start
func minimumRemoval(beans []int) int64 {
	sort.Ints(beans)
	sum := 0
	for i := 0; i < len(beans); i++ {
		sum += beans[i]
	}
	ret := sum - len(beans)*beans[0]
	pre := 0
	for i := 1; i < len(beans); i++ {
		pre += beans[i-1]
		tmp := sum - ((len(beans) - i) * beans[i])
		if tmp < ret {
			ret = tmp
		}
	}
	return int64(ret)
}

// func main() {
// fmt.Println(minimumRemoval([]int{4, 1, 6, 5}), minimumRemoval([]int{2, 10, 3, 2}))
// }

// @lc code=end
