/*
 * @lc app=leetcode.cn id=1539 lang=golang
 *
 * [1539] 第 k 个缺失的正整数
 */

// @lc code=start
package main

func findKthPositive(arr []int, k int) int {
	pre := 1
	for i := 0; i < len(arr); i++ {
		if arr[i] == pre {
			pre++
		} else {
			if arr[i]-pre >= k {
				return pre + k - 1
			} else {
				k -= arr[i] - pre
				pre = arr[i] + 1
			}
		}
	}
	return arr[len(arr)-1] + k
}

// func main() {
// fmt.Println(findKthPositive([]int{2, 3, 4, 7, 11}, 5))
// }

// @lc code=end
