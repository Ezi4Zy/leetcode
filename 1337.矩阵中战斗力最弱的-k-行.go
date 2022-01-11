/*
 * @lc app=leetcode.cn id=1337 lang=golang
 *
 * [1337] 矩阵中战斗力最弱的 K 行
 */
package main

import (
	"sort"
)

// @lc code=start
func kWeakestRows(mat [][]int, k int) []int {
	arr := make([]int, len(mat))
	for i := 0; i < len(mat); i++ {
		arr[i] = i
	}
	sort.Slice(arr, func(i, j int) bool {
		counti := 0
		countj := 0
		tempi := arr[i]
		tempj := arr[j]
		for m := 0; m < len(mat[tempi]); m++ {
			if mat[tempi][m] == 0 {
				break
			} else {
				counti++
			}
		}
		for n := 0; n < len(mat[tempj]); n++ {
			if mat[tempj][n] == 0 {
				break
			} else {
				countj++
			}
		}
		if counti == countj {
			return tempi < tempj
		} else {
			return counti < countj
		}
	})
	return arr[:k]
}

// @lc code=end
