/*
 * @lc app=leetcode.cn id=812 lang=golang
 *
 * [812] 最大三角形面积
 */
package main

import (
	"math"
)

// @lc code=start
func calArea(point1 []int, point2 []int, point3 []int) float64 {
	return 0.5 * math.Abs(float64(point1[0]*point2[1]+point2[0]*point3[1]+point3[0]*point1[1]-point1[1]*point2[0]-point2[1]*point3[0]-point3[1]*point1[0]))

}
func largestTriangleArea(points [][]int) float64 {
	maxArea := 0.0
	for i := 0; i < len(points)-2; i++ {
		for j := i + 1; j < len(points)-1; j++ {
			for n := i + 2; n < len(points); n++ {
				tmpArea := calArea(points[i], points[j], points[n])
				if tmpArea > maxArea {
					maxArea = tmpArea
				}
			}
		}
	}
	return maxArea
}

// func main() {
// fmt.Println(largestTriangleArea([][]int{
// {0,0},
// {0,1},
// {1,0},
// {0,2},
// {2,0},
// }))
// }

// @lc code=end
