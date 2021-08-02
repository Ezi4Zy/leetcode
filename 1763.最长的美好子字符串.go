/*
 * @lc app=leetcode.cn id=1763 lang=golang
 *
 * [1763] 最长的美好子字符串
 */

// @lc code=start
package main

func longestNiceSubstring(s string) string {
	var ret string
	for i := 0; i < len(s); i++ {
		a, b := 0, 0
		for j := i; j < len(s); j++ {
			if s[j] >= 'a' && s[j] <= 'z' {
				a |= 1 << (s[j] - 'a')
			} else {
				b |= 1 << (s[j] - 'A')
			}
			if a == b && len(ret) < j-i+1 {
				ret = string(s[i : j+1])
			}
		}
	}
	return ret

}

// func main() {
// fmt.Println(longestNiceSubstring("YazaAay"))
// fmt.Println(longestNiceSubstring("dDzeE"))
// }

// @lc code=end
