/*
 * @lc app=leetcode.cn id=1094 lang=golang
 *
 * [1094] 拼车
 */

// @lc code=start
// package leetcode

func carPooling(trips [][]int, capacity int) bool {
	passengers := 0
	startLocationMap := make(map[int]int, 0)
	endLocationMap := make(map[int]int, 0)
	for _, trip := range trips {
		startLocationMap[trip[1]] += trip[0]
		endLocationMap[trip[2]] += trip[0]
	}
	for i := 0; i <= 1000; i++ {
		end, ok := endLocationMap[i]
		if ok {
			passengers -= end
		}
		start, ok := startLocationMap[i]
		if ok {
			passengers += start
		}
		if passengers > capacity {
			return false
		}
	}
	return true
}

// @lc code=end
