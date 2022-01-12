/*
 * @lc app=leetcode.cn id=1287 lang=golang
 *
 * [1287] 有序数组中出现次数超过25%的元素
 */
package main

// @lc code=start
func findSpecialInteger(arr []int) int {
	counter := make(map[int]int, len(arr))
	for i := 0; i < len(arr); i++ {
		counter[arr[i]]++
	}
	for k, v := range counter {
		if v > len(arr)/4 {
			return k
		}
	}
	return -1
}

// func main() {
// fmt.Println(findSpecialInteger([]int{1, 2, 2, 6, 6, 6, 6, 7, 10}))
// }

// @lc code=end
