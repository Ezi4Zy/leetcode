/*
 * @lc app=leetcode.cn id=1909 lang=golang
 *
 * [1909] 删除一个元素使数组严格递增
 */

// @lc code=start
// package leetcode
func canBeIncreasing(nums []int) bool {
	flag := true
	pre1 := 0
	pre2 := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] <= pre2{
			if flag{
				flag = false
				if nums[i] <= pre1{
					continue
				}else {
					pre2 = nums[i]
				}
			}else {
				return false
			}
		}else {
			pre1, pre2 = pre2, nums[i]
		}
	}
	return true
}
// @lc code=end

