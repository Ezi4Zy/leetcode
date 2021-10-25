/*
 * @lc app=leetcode.cn id=1389 lang=golang
 *
 * [1389] 按既定顺序创建目标数组
 */

// @lc code=start
package main

func createTargetArray(nums []int, index []int) []int {
	ret := make([]int, len(nums))
	for k, v := range index {
		copy(ret[v+1:], ret[v:])
		ret[v] = nums[k]
	}
	return ret
}

// func main() {
// fmt.Println(createTargetArray([]int{0, 1, 2, 3, 4}, []int{0, 1, 2, 2, 1}))
// }

// @lc code=end
