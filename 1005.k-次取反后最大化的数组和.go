/*
 * @lc app=leetcode.cn id=1005 lang=golang
 *
 * [1005] K 次取反后最大化的数组和
 */
package main

import (
	"sort"
)

// @lc code=start
func largestSumAfterKNegations(nums []int, k int) int {
	sort.Ints(nums)
	ret := 0
	maxNegativeNumIndex := -1
	for i := 0; i < len(nums); i++ {
		if k > 0 {
			if nums[i] < 0 {
				k--
				ret -= nums[i]
				maxNegativeNumIndex = i
			} else {
				if nums[i] == 0 {
					k = 0
				} else {
					if k%2 != 0 {
						if maxNegativeNumIndex != -1 && nums[i] > -nums[maxNegativeNumIndex] {
							ret += nums[i] + 2*nums[maxNegativeNumIndex]
						} else {
							ret -= nums[i]
						}
					} else {
						ret += nums[i]
					}
					k = 0
				}
			}
		} else {
			ret += nums[i]
		}
	}
	if k%2 != 0 {
		ret += nums[maxNegativeNumIndex] * 2
	}
	return ret
}

// func main() {
// fmt.Println(largestSumAfterKNegations([]int{4, 2, 3}, 1), largestSumAfterKNegations([]int{3, -1, 0, 2}, 3),
// largestSumAfterKNegations([]int{2, -3, -1, 5, -4}, 2))
// }

// @lc code=end
