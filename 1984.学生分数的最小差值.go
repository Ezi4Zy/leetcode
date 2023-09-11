/*
 * @lc app=leetcode.cn id=1984 lang=golang
 *
 * [1984] 学生分数的最小差值
 */

package main

import (
	"fmt"
	"sort"
)

// @lc code=start
func minimumDifference(nums []int, k int) int {
	sort.Ints(nums)
	ret := nums[k-1] - nums[0]
	for i := 1; i <= len(nums)-k; i++ {
		if nums[i+k-1]-nums[i] < ret {
			ret = nums[i+k-1] - nums[i]
		}
	}
	return ret
}

// @lc code=end

func main() {
	fmt.Println(minimumDifference([]int{90}, 1))
	fmt.Println(minimumDifference([]int{9, 4, 1, 7}, 2))
}
