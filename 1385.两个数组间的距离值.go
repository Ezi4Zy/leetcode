/*
 * @lc app=leetcode.cn id=1385 lang=golang
 *
 * [1385] 两个数组间的距离值
 */

// @lc code=start
package main

import "math"

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	count := 0
	for i := 0; i < len(arr1); i++ {
		flag := true
		for j := 0; j < len(arr2); j++ {
			if int(math.Abs(float64(arr1[i]-arr2[j]))) <= d {
				flag = false
				break
			}
		}
		if flag {
			count++
		}
	}
	return count
}

// @lc code=end
