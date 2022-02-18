/*
 * @lc app=leetcode.cn id=1184 lang=golang
 *
 * [1184] 公交站间的距离
 */
package main

// @lc code=start
func distanceBetweenBusStops(distance []int, start int, destination int) int {
	clockwiseDistance := 0
	anticlockwiseDistance := 0
	index := start
	for index != destination {
		clockwiseDistance += distance[index]
		index = (index + 1) % len(distance)
	}
	for index != start {
		anticlockwiseDistance += distance[index]
		index = (index + 1) % len(distance)
	}
	if clockwiseDistance < anticlockwiseDistance {
		return clockwiseDistance
	} else {
		return anticlockwiseDistance
	}
}

// func main() {
// fmt.Println(distanceBetweenBusStops([]int{1, 2, 3, 4}, 0, 1),
// distanceBetweenBusStops([]int{1, 2, 3, 4}, 0, 2),
// distanceBetweenBusStops([]int{1, 2, 3, 4}, 0, 3))
// }

// @lc code=end
