/*
 * @lc app=leetcode.cn id=852 lang=golang
 *
 * [852] 山脉数组的峰顶索引
 */
package main

// @lc code=start
func peakIndexInMountainArray(arr []int) int {
	for i := 1; i < len(arr); i++ {
		if arr[i] < arr[i-1] {
			return i - 1
		}
	}
	return -1
}

// func main() {
// fmt.Println(peakIndexInMountainArray([]int{0, 1, 0}))
// }

// @lc code=end
