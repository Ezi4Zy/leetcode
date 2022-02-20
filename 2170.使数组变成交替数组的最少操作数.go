/*
 * @lc app=leetcode.cn id=2170 lang=golang
 *
 * [2170] 使数组变成交替数组的最少操作数
 */
package main

import (
	"math"
)

// @lc code=start
func minimumOperations(nums []int) int {
	if len(nums) == 1 {
		return 0
	}
	oddIndexNumsMap := make(map[int]int, len(nums)/2)
	evenIndexNumsMap := make(map[int]int, len(nums)/2+len(nums)%2)
	for i := 0; i < len(nums); i++ {
		if i%2 == 0 {
			evenIndexNumsMap[nums[i]]++
		} else {
			oddIndexNumsMap[nums[i]]++
		}
	}
	firstOddIndexNum := 0
	firstOddIndexNumCount := 0
	secondOddIndexNumCount := 0
	for num, count := range oddIndexNumsMap {
		if count > firstOddIndexNumCount {
			firstOddIndexNum, firstOddIndexNumCount, secondOddIndexNumCount = num, count, firstOddIndexNumCount
		} else {
			if count == firstOddIndexNumCount || count > secondOddIndexNumCount {
				secondOddIndexNumCount = count
			}
		}
	}
	firstEvenIndexNum := 0
	firstEvenIndexNumCount := 0
	secondEvenIndexNumCount := 0
	for num, count := range evenIndexNumsMap {
		if count > firstEvenIndexNumCount {
			firstEvenIndexNum, firstEvenIndexNumCount, secondEvenIndexNumCount = num, count, firstEvenIndexNumCount
		} else {
			if count == firstEvenIndexNumCount || count > secondEvenIndexNumCount {
				secondEvenIndexNumCount = count
			}
		}
	}
	if firstEvenIndexNum != firstOddIndexNum {
		return len(nums) - firstEvenIndexNumCount - firstOddIndexNumCount
	}
	return len(nums) - int(math.Max(float64(firstEvenIndexNumCount+secondOddIndexNumCount), float64(firstOddIndexNumCount+secondEvenIndexNumCount)))

}

// func main() {
// fmt.Println(minimumOperations([]int{3, 1, 3, 2, 4, 3}),
// minimumOperations([]int{1, 2, 2, 2, 2}))
// }

// @lc code=end
