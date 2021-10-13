/*
 * @lc app=leetcode.cn id=1496 lang=golang
 *
 * [1496] 判断路径是否相交
 */

// @lc code=start
package main

import "fmt"

func isPathCrossing(path string) bool {
	pointMap := make(map[string]bool, 0)
	cur := "0|0"
	x := 0
	y := 0
	pointMap[cur] = true
	for i := 0; i < len(path); i++ {
		switch path[i] {
		case 'N':
			y += 1
		case 'S':
			y -= 1
		case 'E':
			x += 1
		case 'W':
			x -= 1
		}
		point := fmt.Sprint(x) + "|" + fmt.Sprint(y)
		if pointMap[point] {
			return true
		} else {
			pointMap[point] = true
		}
	}
	return false
}

// func main() {
// fmt.Println(isPathCrossing("NES"))
// fmt.Println(isPathCrossing("NESWW"))
// }

// @lc code=end
