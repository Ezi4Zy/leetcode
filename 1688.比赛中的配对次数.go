/*
 * @lc app=leetcode.cn id=1688 lang=golang
 *
 * [1688] 比赛中的配对次数
 */

// @lc code=start
package main

func numberOfMatches(n int) int {
	if n < 2 {
		return 0
	} else {
		return n/2 + numberOfMatches((n+1)/2)
	}

}

// func main() {
// fmt.Println(numberOfMatches(14))
// }

// @lc code=end
