/*
 * @lc app=leetcode.cn id=1732 lang=golang
 *
 * [1732] 找到最高海拔
 */

// @lc code=start
package main

func largestAltitude(gain []int) int {
	ret := 0
	if gain[0] > 0 {
		ret = gain[0]
	}
	for i := 1; i < len(gain); i++ {
		gain[i] += gain[i-1]
		if gain[i] > ret {
			ret = gain[i]
		}
	}
	return ret

}

// @lc code=end
