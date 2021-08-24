/*
 * @lc app=leetcode.cn id=1566 lang=golang
 *
 * [1566] 重复至少 K 次且长度为 M 的模式
 */

// @lc code=start
package main

func containsPattern(arr []int, m int, k int) bool {
	for i := 0; i < len(arr)-m*k+1; i++ {
		flag := true
		for j := i; j < i+m*k; j++ {
			if arr[j] != arr[i+(j-i)%m] {
				flag = false
				break
			}
		}
		if flag {
			return true
		}
	}
	return false
}

// func main() {
// fmt.Println(containsPattern([]int{1, 2, 4, 4, 4, 4}, 1, 3))
// fmt.Println(containsPattern([]int{1, 2, 1, 2, 1, 1, 1, 3}, 2, 2))
// fmt.Println(containsPattern([]int{1, 2, 1, 2, 1, 3}, 2, 3))
// fmt.Println(containsPattern([]int{1, 2, 3, 1, 2}, 2, 2))
// fmt.Println(containsPattern([]int{2, 2, 2, 2}, 2, 3))
// }

// @lc code=end
