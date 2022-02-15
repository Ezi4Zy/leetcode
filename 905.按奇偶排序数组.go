/*
 * @lc app=leetcode.cn id=905 lang=golang
 *
 * [905] 按奇偶排序数组
 */
package main

// @lc code=start
func sortArrayByParity(nums []int) []int {
	odd := 0
	even := 0
	for {
		for odd < len(nums) && nums[odd]%2 != 1 {
			odd++
		}
		if odd > even {
			even = odd + 1
		}
		for even < len(nums) && nums[even]%2 != 0 {
			even++
		}
		if odd < len(nums) && even < len(nums) {
			nums[odd], nums[even] = nums[even], nums[odd]
			odd++
		} else {
			break
		}
	}
	return nums
}

// func main() {
// fmt.Println(sortArrayByParity([]int{3, 1, 2, 4}))
// }

// @lc code=end
