/*
 * @lc app=leetcode.cn id=1876 lang=golang
 *
 * [1876] 长度为三且各字符不同的子字符串
 */

// @lc code=start

// package leetcode

func countGoodSubstrings(s string) int {
	ret := 0
	b := []byte(s)
	for i := 0; i < len(b)-2; i++ {
		temp := make(map[byte]bool)
		flag := true
		for j := 0; j < 3; j++ {
			_, ok := temp[b[i+j]]
			if ok {
				flag = false
				break
			} else {
				temp[b[i+j]] = true
			}
		}
		if flag {
			ret += 1
		}
	}
	return ret
}

// @lc code=end
