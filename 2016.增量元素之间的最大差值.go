/*
 * @lc app=leetcode.cn id=2016 lang=golang
 *
 * [2016] 增量元素之间的最大差值
 */

package main

import "fmt"

// @lc code=start
func maximumDifference(nums []int) int {
	ret := -1
	minNum := nums[0]
	for _, num := range nums {
		if num < minNum {
			minNum = num
		} else {
			if num-minNum > 0 && num-minNum > ret {
				ret = num - minNum
			}
		}
	}
	return ret
}

func maximumDifference1(nums []int) int {
	ret := -1
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[j] > nums[i] {
				if nums[j]-nums[i] > ret {
					ret = nums[j] - nums[i]
				}
			}
		}
	}
	return ret
}

// @lc code=end

func main() {
	fmt.Println(maximumDifference([]int{7, 1, 5, 4}))
	fmt.Println(maximumDifference([]int{9, 4, 3, 2}))
	fmt.Println(maximumDifference([]int{1, 5, 2, 10}))
}
