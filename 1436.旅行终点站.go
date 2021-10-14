/*
 * @lc app=leetcode.cn id=1436 lang=golang
 *
 * [1436] 旅行终点站
 */

// @lc code=start
package main

func destCity(paths [][]string) string {
	pathMap := make(map[string]bool)
	for i := 0; i < len(paths); i++ {
		pathMap[paths[i][0]] = true
	}
	for _, path := range paths {
		if !pathMap[path[1]] {
			return path[1]
		}
	}
	return ""
}

// @lc code=end
