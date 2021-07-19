/*
 * @lc app=leetcode.cn id=1399 lang=golang
 *
 * [1399] 统计最大组的数目
 */

// @lc code=start
// package main

func countLargestGroup(n int) int {
	maxCount := 0
	counter := make(map[int]int, 0)
	for i := 1; i <= n; i++ {
		j, i0 := 0, i
		for i0 > 0 {
			j += i0 % 10
			i0 /= 10
		}
		counter[j]++
		if counter[j] > maxCount {
			maxCount = counter[j]
		}
	}
	ret := 0
	for _, v := range counter {
		if v == maxCount {
			ret++
		}
	}
	return ret
}


// @lc code=end
