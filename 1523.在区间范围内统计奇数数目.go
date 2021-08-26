/*
 * @lc app=leetcode.cn id=1523 lang=golang
 *
 * [1523] 在区间范围内统计奇数数目
 */

// @lc code=start
package main

func countOdds(low int, high int) int {
	return (high-low)/2 + ((high-low+1)%2)*(high%2) + (high-low)%2

}

// func main() {
// fmt.Println(countOdds(3, 7),
// countOdds(3, 3),
// countOdds(3, 4),
// countOdds(3, 8),
// countOdds(8, 10),
// countOdds(8, 11))
// }

// @lc code=end
