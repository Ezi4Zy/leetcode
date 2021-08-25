/*
 * @lc app=leetcode.cn id=1534 lang=golang
 *
 * [1534] 统计好三元组
 */

// @lc code=start
package main

import (
	"math"
)

func countGoodTriplets(arr []int, a int, b int, c int) int {
	count := 0
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			for k := j + 1; k < len(arr); k++ {
				if int(math.Abs(float64(arr[i]-arr[j]))) <= a &&
					int(math.Abs(float64(arr[j]-arr[k]))) <= b &&
					int(math.Abs(float64(arr[i]-arr[k]))) <= c {
					count++
				}
			}
		}
	}
	return count
}

// func main() {
// fmt.Println(countGoodTriplets([]int{3, 0, 1, 1, 9, 7}, 7, 2, 3))
// }

// @lc code=end
