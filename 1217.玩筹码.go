/*
 * @lc app=leetcode.cn id=1217 lang=golang
 *
 * [1217] 玩筹码
 */
package main

// @lc code=start
func minCostToMoveChips(position []int) int {
	evenCount := 0
	oddCount := 0
	for i := 0; i < len(position); i++ {
		if position[i]%2 == 0 {
			evenCount++
		} else {
			oddCount++
		}
	}
	if evenCount > oddCount {
		return oddCount
	} else {
		return evenCount
	}
}

// @lc code=end
