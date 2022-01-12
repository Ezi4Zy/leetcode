/*
 * @lc app=leetcode.cn id=1331 lang=golang
 *
 * [1331] 数组序号转换
 */
package main

import (
	"sort"
)

// @lc code=start
func arrayRankTransform(arr []int) []int {
	if len(arr) == 0 {
		return arr
	}
	tmpArr := make([]int, len(arr))
	for i := 0; i < len(arr); i++ {
		tmpArr[i] = arr[i]
	}
	sort.Ints(tmpArr)
	indexMap := make(map[int]int, len(arr))
	pre := tmpArr[0]
	indexMap[tmpArr[0]] = 1
	for i := 1; i < len(arr); i++ {
		if tmpArr[i] != pre {
			indexMap[tmpArr[i]] = indexMap[pre] + 1
			pre = tmpArr[i]
		}
	}
	for i := 0; i < len(arr); i++ {
		arr[i] = indexMap[arr[i]]
	}
	return arr
}

// func main() {
// fmt.Println(arrayRankTransform([]int{40, 10, 20, 30}))
// fmt.Println(arrayRankTransform([]int{100, 100, 100}))
// fmt.Println(arrayRankTransform([]int{37, 12, 28, 9, 100, 56, 80, 5, 12}))
// }

// @lc code=end
