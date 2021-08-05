/*
 * @lc app=leetcode.cn id=1720 lang=golang
 *
 * [1720] 解码异或后的数组
 */

// @lc code=start
package main

func decode(encoded []int, first int) []int {
	ret := make([]int, len(encoded)+1)
	ret[0] = first
	for i := 0; i < len(encoded); i++ {
		ret[i+1] = encoded[i] ^ ret[i]
	}
	return ret

}

// @lc code=end
