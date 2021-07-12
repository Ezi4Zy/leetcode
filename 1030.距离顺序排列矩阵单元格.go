/*
 * @lc app=leetcode.cn id=1030 lang=golang
 *
 * [1030] 距离顺序排列矩阵单元格
 */

// @lc code=start
// package leetcode

import (
	"math"
	"sort"
)
func allCellsDistOrder(rows int, cols int, rCenter int, cCenter int) [][]int {
	ret := make([][]int, rows * cols )
	map_ := make(map[int][][]int)
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			dis := int(math.Abs(float64(i - rCenter)) + math.Abs(float64(j - cCenter)))
			elem := []int{i, j}
			map_[dis] = append(map_[dis], elem)
		}
	}
	keys := make([]int, 0, len(map_))
	for k := range map_ {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	index := 0
	for key := range keys {
		for i := 0; i < len(map_[key]); i++ {
			ret[index] = map_[key][i]
			index += 1
		}

	}
	return ret

}
// @lc code=end

