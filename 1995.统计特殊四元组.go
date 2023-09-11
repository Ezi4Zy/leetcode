/*
 * @lc app=leetcode.cn id=1995 lang=golang
 *
 * [1995] 统计特殊四元组
 */
package main

import "fmt"

// @lc code=start
func countQuadruplets(nums []int) int {
	count := 0
	for i := 0; i < len(nums)-3; i++ {
		for j := i + 1; j < len(nums)-2; j++ {
			for m := j + 1; m < len(nums)-1; m++ {
				for n := m + 1; n < len(nums); n++ {
					if nums[i]+nums[j]+nums[m] == nums[n] {
						count++
					}
				}
			}
		}
	}
	return count
}

// @lc code=end

func main() {
	fmt.Println(countQuadruplets([]int{1, 2, 3, 6}))
	fmt.Println(countQuadruplets([]int{3, 3, 6, 4, 5}))
	fmt.Println(countQuadruplets([]int{1, 1, 1, 3, 5}))
}
