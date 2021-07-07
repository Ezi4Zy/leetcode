/*
 * @lc app=leetcode.cn id=1524 lang=golang
 *
 * [1524] 和为奇数的子数组数目
 */

// @lc code=start
// package leetcode

func numOfSubarrays(arr []int) int {
	oddNums := 0
	evenNums := 1
	var res = 0
	sum := 0
	for _, num := range arr {
		sum += num
		if sum%2 == 1 {
			res += evenNums
			oddNums += 1
		} else {
			res += oddNums
			evenNums += 1
		}
	}
	return res % 1000000007
}

// @lc code=end
