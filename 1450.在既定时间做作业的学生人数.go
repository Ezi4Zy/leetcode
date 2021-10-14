/*
 * @lc app=leetcode.cn id=1450 lang=golang
 *
 * [1450] 在既定时间做作业的学生人数
 */

// @lc code=start
package main

func busyStudent(startTime []int, endTime []int, queryTime int) int {
	ret := 0
	for i := 0; i < len(startTime); i++ {
		if queryTime >= startTime[i] && queryTime <= endTime[i] {
			ret++
		}
	}
	return ret
}

// @lc code=end
