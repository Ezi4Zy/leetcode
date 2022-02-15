/*
 * @lc app=leetcode.cn id=976 lang=golang
 *
 * [976] 三角形的最大周长
 */
package main

import "sort"

// @lc code=start
func largestPerimeter(nums []int) int {
	maxPerimeter := 0
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})
	for i := 0; i < len(nums); i++ {
		if maxPerimeter/3 > nums[i] {
			return maxPerimeter
		}
		for j := i + 1; j < len(nums); j++ {
			if (maxPerimeter-nums[i])/2 > nums[j] {
				break
			}
			for m := j + 1; m < len(nums); m++ {
				if nums[m]+nums[j] > nums[i] {
					perimeter := nums[i] + nums[j] + nums[m]
					if perimeter > maxPerimeter {
						maxPerimeter = perimeter
					}
				} else {
					break
				}
			}

		}
	}
	return maxPerimeter
}

// @lc code=end
