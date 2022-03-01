/*
 * @lc app=leetcode.cn id=807 lang=golang
 *
 * [807] 保持城市天际线
 */
package main

import (
	"math"
)

// @lc code=start
func maxIncreaseKeepingSkyline(grid [][]int) int {
	maxRow := make([]int, len(grid))
	maxCol := make([]int, len(grid[0]))
	for i := 0; i < len(grid); i++ {
		maxRow[i] = grid[i][0]
		for j := 1; j < len(grid[i]); j++ {
			if grid[i][j] > maxRow[i] {
				maxRow[i] = grid[i][j]
			}
		}
	}
	for j := 0; j < len(grid[0]); j++ {
		maxCol[j] = grid[0][j]
		for i := 0; i < len(grid); i++ {
			if grid[i][j] > maxCol[j] {
				maxCol[j] = grid[i][j]
			}
		}
	}
	ret := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			ret += int(math.Min(float64(maxRow[i]), float64(maxCol[j]))) - grid[i][j]
		}
	}
	return ret
}

// func main() {
// fmt.Println(maxIncreaseKeepingSkyline([][]int{
// {3, 0, 8, 4},
// {2, 4, 5, 7},
// {9, 2, 6, 3},
// {0, 3, 1, 0},
// }))
// fmt.Println(maxIncreaseKeepingSkyline([][]int{
// {0, 0, 0, 0},
// {0, 0, 0, 0},
// {0, 0, 0, 0},
// {0, 0, 0, 0},
// }))
// }

// @lc code=end
