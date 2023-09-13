/*
 * @lc app=leetcode.cn id=2037 lang=golang
 *
 * [2037] 使每位学生都有座位的最少移动次数
 */

package main

import (
	"fmt"
	"sort"
)

// @lc code=start
func minMovesToSeat(seats []int, students []int) int {
	count := 0
	sort.Ints(seats)
	sort.Ints(students)
	for i := 0; i < len(seats); i++ {
		if seats[i] < students[i] {
			count += students[i] - seats[i]
		} else {
			count += seats[i] - students[i]
		}
	}
	return count
}

// @lc code=end

func main() {
	fmt.Println(minMovesToSeat([]int{3, 1, 5}, []int{2, 7, 4}))
	fmt.Println(minMovesToSeat([]int{4, 1, 5, 9}, []int{1, 3, 2, 6}))
	fmt.Println(minMovesToSeat([]int{2, 2, 6, 6}, []int{1, 3, 2, 6}))
}
