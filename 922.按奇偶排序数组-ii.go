/*
 * @lc app=leetcode.cn id=922 lang=golang
 *
 * [922] 按奇偶排序数组 II
 */
package main

// @lc code=start
func sortArrayByParityII(nums []int) []int {
	oddIndex := 1
	evenIndex := 0
	for {
		for oddIndex < len(nums) && nums[oddIndex]%2 == 1 {
			oddIndex += 2
		}
		for evenIndex < len(nums) && nums[evenIndex]%2 == 0 {
			evenIndex += 2
		}
		if oddIndex < len(nums) && evenIndex < len(nums) {
			nums[oddIndex], nums[evenIndex] = nums[evenIndex], nums[oddIndex]
			oddIndex += 2
			evenIndex += 2
		} else {
			break
		}
	}
	return nums
}

// func main() {
// fmt.Println(sortArrayByParityII([]int{4, 2, 5, 7}), sortArrayByParityII([]int{2, 3}))
// }

// @lc code=end
