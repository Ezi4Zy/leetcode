/*
 * @lc app=leetcode.cn id=1664 lang=golang
 *
 * [1664] 生成平衡数组的方案数
 */

// @lc code=start
// package leetcode

func waysToMakeFair(nums []int) int {
	result, odd, even := 0, 0, 0
	for i, n := range nums {
		if i&1 == 0 {
			even += n
		} else {
			odd += n
		}
	}
	newOdd, newEven := 0, 0
	for i, n := range nums {
		if i&1 == 0 {
			even -= n
		} else {
			odd -= n
		}
		if odd+newOdd == even+newEven {
			result++
		}
		if i&1 == 0 {
			newOdd += n
		} else {
			newEven += n
		}
	}
	return result

}

// @lc code=end
