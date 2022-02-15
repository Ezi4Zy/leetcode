/*
 * @lc app=leetcode.cn id=941 lang=golang
 *
 * [941] 有效的山脉数组
 */
package main

// @lc code=start
func validMountainArray(arr []int) bool {
	if len(arr) < 3 || arr[1] <= arr[0] {
		return false
	}

	isLeft := true
	for i := 2; i < len(arr); i++ {
		if arr[i] > arr[i-1] {
			if !isLeft {
				return false
			}
		} else {
			if arr[i] == arr[i-1] {
				return false
			} else {
				isLeft = false
			}
		}
	}
	return !isLeft
}

// func main() {
// fmt.Println(validMountainArray([]int{2, 1}),
// validMountainArray([]int{3, 5, 5}),
// validMountainArray([]int{0, 3, 2, 1}))
// }

// @lc code=end
