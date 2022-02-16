/*
 * @lc app=leetcode.cn id=1018 lang=golang
 *
 * [1018] 可被 5 整除的二进制前缀
 */
package main

// @lc code=start
func prefixesDivBy5(nums []int) []bool {
	num := 0
	ret := make([]bool, len(nums))
	for i := 0; i < len(nums); i++ {
		num = (num*2 + nums[i]) % 5
		if num == 0 {
			ret[i] = true
		}
	}
	return ret
}

// func main() {
	// fmt.Println(prefixesDivBy5([]int{0, 1, 1}),
		// prefixesDivBy5([]int{0, 1, 1, 1, 1, 1}), prefixesDivBy5([]int{1, 1, 1, 0, 1}))
// }

// @lc code=end
