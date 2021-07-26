/*
 * @lc app=leetcode.cn id=1863 lang=golang
 *
 * [1863] 找出所有子集的异或总和再求和
 */

// @lc code=start
// package main
//
// import "fmt"

func subsetXORSum(nums []int) int {
	ret := 0
	n := len(nums)
	var dfs func(val int, idx int)
	dfs = func(val int, idx int) {
		if idx >= n {
			ret += val
			return
		}
		dfs(val, idx+1)
		dfs(val^nums[idx], idx+1)
	}
	dfs(0, 0)

	return ret
}

// func main() {
// nums := []int{1, 3}
// fmt.Println(subsetXORSum(nums))
// nums = []int{5, 1, 6}
// fmt.Println(subsetXORSum(nums))
// nums = []int{3, 4, 5, 6, 7, 8}
// fmt.Println(subsetXORSum(nums))
// }

// @lc code=end
