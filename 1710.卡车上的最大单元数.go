/*
 * @lc app=leetcode.cn id=1710 lang=golang
 *
 * [1710] 卡车上的最大单元数
 */

// @lc code=start
package main

import (
	"sort"
)

type boxType [][]int

func (b boxType) Len() int {
	return len(b)
}
func (b boxType) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}
func (b boxType) Less(i, j int) bool {
	return b[i][1] > b[j][1]
}

func maximumUnits(boxTypes [][]int, truckSize int) int {
	ret := 0
	sort.Sort(boxType(boxTypes))
	for i := 0; i < len(boxTypes); i++ {
		if boxTypes[i][0] < truckSize {
			ret += boxTypes[i][0] * boxTypes[i][1]
		} else {
			ret += truckSize * boxTypes[i][1]
			break
		}
		truckSize -= boxTypes[i][0]
	}
	return ret
}

// @lc code=end
