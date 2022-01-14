/*
 * @lc app=leetcode.cn id=1207 lang=golang
 *
 * [1207] 独一无二的出现次数
 */
package main

// @lc code=start
func uniqueOccurrences(arr []int) bool {
	counter := make(map[int]int)
	for i := 0; i < len(arr); i++ {
		counter[arr[i]]++
	}
	occu := make(map[int]bool)
	for _, v := range counter {
		if occu[v] {
			return false
		} else {
			occu[v] = true
		}
	}
	return true
}

// func main() {
// fmt.Println(uniqueOccurrences([]int{1, 2, 2, 1, 1, 3}))
// fmt.Println(uniqueOccurrences([]int{1, 2}))
// fmt.Println(uniqueOccurrences([]int{-3, 0, 1, -3, 1, 1, 1, -3, 10, 0}))
// }

// @lc code=end
