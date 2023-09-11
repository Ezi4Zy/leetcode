/*
 * @lc app=leetcode.cn id=2006 lang=golang
 *
 * [2006] 差的绝对值为 K 的数对数目
 */

package main

import "fmt"

// @lc code=start
func countKDifference(nums []int, k int) int {
	counter := make(map[int]int, 0)
	ret := 0
	for _, num := range nums {
		ret += counter[num-k] + counter[num+k]
		counter[num]++
	}
	return ret
}

// @lc code=end



func main() {
	fmt.Println(countKDifference([]int{1, 2, 2, 1}, 1))
	fmt.Println(countKDifference([]int{1, 3}, 3))
	fmt.Println(countKDifference([]int{3, 2, 1, 5, 4}, 2))
}
