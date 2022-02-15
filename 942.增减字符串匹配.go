/*
 * @lc app=leetcode.cn id=942 lang=golang
 *
 * [942] 增减字符串匹配
 */
package main

// @lc code=start
func diStringMatch(s string) []int {
	ret := make([]int, len(s)+1)
	start := 0
	end := len(s)
	for i := 0; i < len(s); i++ {
		if s[i] == 'I' {
			ret[i] = start
			start++
		} else {
			ret[i] = end
			end--
		}
	}
	if s[len(s)-1] == 'I' {
		ret[len(s)] = ret[len(s)-1] + 1
	} else {
		ret[len(s)] = ret[len(s)-1] - 1
	}
	return ret
}

// func main() {
// fmt.Println(diStringMatch("IDID"), diStringMatch("III"), diStringMatch("DDI"))
// }

// @lc code=end
