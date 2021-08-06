/*
 * @lc app=leetcode.cn id=1700 lang=golang
 *
 * [1700] 无法吃午餐的学生数量
 */

// @lc code=start
package main

func countStudents(students []int, sandwiches []int) int {
	count := [2]int{}
	for i := 0; i < len(students); i++ {
		count[students[i]]++
	}
	for i := 0; i < len(sandwiches); i++ {
		if count[sandwiches[i]] > 0 {
			count[sandwiches[i]]--
		} else {
			break
		}
	}
	return count[0] + count[1]
}

// @lc code=end
