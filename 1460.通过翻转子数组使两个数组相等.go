/*
 * @lc app=leetcode.cn id=1460 lang=golang
 *
 * [1460] 通过翻转子数组使两个数组相等
 */

// @lc code=start
package main

func canBeEqual(target []int, arr []int) bool {
	count := make(map[int]int)
	for i := 0; i < len(target); i++ {
		count[target[i]] += 1
	}
	for i := 0; i < len(arr); i++ {
		count[arr[i]] -= 1
		if count[arr[i]] < 0 {
			return false
		}
	}
	return true
}

// @lc code=end
