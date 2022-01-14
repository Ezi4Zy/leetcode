/*
 * @lc app=leetcode.cn id=1221 lang=golang
 *
 * [1221] 分割平衡字符串
 */
package main

// @lc code=start
func balancedStringSplit(s string) int {
	count := 0
	balance := 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'L' {
			balance++
		} else {
			balance--
		}
		if balance == 0 {
			count++
		}
	}
	return count
}

// func main() {
// fmt.Println(balancedStringSplit("RLRRLLRLRL"))
// fmt.Println(balancedStringSplit("RLLLLRRRLR"))
// fmt.Println(balancedStringSplit("LLLLRRRR"))
// fmt.Println(balancedStringSplit("RLRRRLLRLL"))
// }

// @lc code=end
