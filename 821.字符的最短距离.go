/*
 * @lc app=leetcode.cn id=821 lang=golang
 *
 * [821] 字符的最短距离
 */
package main

// @lc code=start
func shortestToChar(s string, c byte) []int {
	ret := make([]int, len(s))
	for i := 0; i < len(s); i++ {
		if s[i] == c {
			ret[i] = 0
		} else {
			ret[i] = len(s)
		}
	}
	for i := 1; i < len(s); i++ {
		for j := 0; j < len(s); j++ {
			if ret[j] >= i {
				if j > 0 && ret[j-1] == i-1 {
					ret[j] = i
				}
				if j < len(s)-1 && ret[j+1] == i-1 {
					ret[j] = i
				}
			}
		}
	}
	return ret
}

// func main(){
// fmt.Println(shortestToChar("loveleetcode", 'e'))
// }

// @lc code=end
