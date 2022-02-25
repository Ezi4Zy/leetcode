/*
 * @lc app=leetcode.cn id=10 lang=golang
 *
 * [10] 正则表达式匹配
 */
package main

// @lc code=start

func isMatch(s string, p string) bool {
	sLen := len(s)
	pLen := len(p)
	ret := make([][]bool, sLen+1)
	for i := 0; i < len(ret); i++ {
		ret[i] = make([]bool, pLen+1)
	}
	ret[0][0] = true
	for i := 0; i < pLen; i++ {
		if p[i] == '*' {
			ret[0][i+1] = ret[0][i-1]
		}
	}
	// fmt.Println(ret[0])
	for i := 0; i < sLen; i++ {
		for j := 0; j < pLen; j++ {
			if p[j] == '*' {
				ret[i+1][j+1] = ret[i+1][j-1] || (ret[i][j+1] && (p[j-1] == s[i] || p[j-1] == '.'))
			} else {
				ret[i+1][j+1] = (s[i] == p[j] || p[j] == '.') && ret[i][j]
			}
		}
		// fmt.Println(i+1, ret[i+1])
	}
	return ret[sLen][pLen]

}

// func main() {
// fmt.Println(isMatch("aa", "a"))
// fmt.Println(isMatch("aa", "a*"))
// fmt.Println(isMatch("ab", ".*"))
// fmt.Println(isMatch("aab", "c*a*b"))
// fmt.Println(isMatch("mississippi", "mis*is*ip*."))
// fmt.Println(isMatch("aaa", "ab*a*c*a"))
// }

// @lc code=end
