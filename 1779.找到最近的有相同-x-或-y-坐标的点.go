/*
 * @lc app=leetcode.cn id=1779 lang=golang
 *
 * [1779] 找到最近的有相同 X 或 Y 坐标的点
 */

// @lc code=start
// package main

func nearestValidPoint(x int, y int, points [][]int) int {
	ret := -1
	distance := 20000
	for i := 0; i < len(points); i++ {
		if points[i][0] == x || points[i][1] == y {
			tmp := 0
			if points[i][0] > x {
				tmp += points[i][0] - x
			} else {
				tmp += x - points[i][0]
			}
			if points[i][1] > y {
				tmp += points[i][1] - y
			} else {
				tmp += y - points[i][1]
			}
			if tmp < distance {
				ret = i
				distance = tmp
			}
		}
	}
	return ret

}

// func main() {
// var points [][]int
// points = append(points, []int{1, 2}, []int{3, 1}, []int{2, 4}, []int{2, 3})
// fmt.Println(nearestValidPoint(3, 4, points))
// }

// @lc code=end
