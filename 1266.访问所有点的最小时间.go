/*
 * @lc app=leetcode.cn id=1266 lang=golang
 *
 * [1266] 访问所有点的最小时间
 */
package main

import (
	"math"
)

// @lc code=start
func minTimeToVisitAllPoints(points [][]int) int {
	ret := 0
	for i := 1; i < len(points); i++ {
		ret += int(math.Max(math.Abs(float64(points[i][0]-points[i-1][0])), math.Abs(float64(points[i][1]-points[i-1][1]))))
	}
	return ret
}

// func main() {
// fmt.Println(minTimeToVisitAllPoints([][]int{
// {1, 1},
// {3, 4},
// {-1, 0},
// }))
// fmt.Println(minTimeToVisitAllPoints([][]int{
// {3, 2},
// {-2, 2},
// }))
// }

// @lc code=end
