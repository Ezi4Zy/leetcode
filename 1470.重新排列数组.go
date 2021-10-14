/*
 * @lc app=leetcode.cn id=1470 lang=golang
 *
 * [1470] 重新排列数组
 */

// @lc code=start
package main

func shuffle(nums []int, n int) []int {
	ret := make([]int, 2*n)
	for i := 0; i < n; i++ {
		ret[i*2] = nums[i]
		ret[i*2+1] = nums[i+n]
	}
	return ret
}

//
// func main() {
// fmt.Println(shuffle([]int{1, 2, 3, 4, 4, 3, 2, 1}, 4))
// fmt.Println(shuffle([]int{2, 5, 1, 3, 4, 7}, 3))
// fmt.Println(shuffle([]int{1, 1, 2, 2}, 2))
// }

// @lc code=end
