/*
 * @lc app=leetcode.cn id=1550 lang=golang
 *
 * [1550] 存在连续三个奇数的数组
 */

// @lc code=start
package main

func threeConsecutiveOdds(arr []int) bool {
	count := 0
	index := 0
	for !(count == 3 || index == len(arr)) {
		if arr[index]%2 == 1 {
			count++
		} else {
			count = 0
		}
		index++
	}
	return count == 3
}

// func main() {
// fmt.Println(threeConsecutiveOdds([]int{2, 4, 6, 1}),
// threeConsecutiveOdds([]int{1, 2, 34, 3, 4, 5, 7, 23, 12}))
// }

// @lc code=end
