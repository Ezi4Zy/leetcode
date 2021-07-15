/*
 * @lc app=leetcode.cn id=1790 lang=golang
 *
 * [1790] 仅执行一次字符串交换能否使两个字符串相等
 */

// @lc code=start
// package leetcode

func areAlmostEqual(s1 string, s2 string) bool {
	try := false
	changeIndex := [2]int{}
	index := 0
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			if try {
				return false
			}
			changeIndex[index] = i
			index++
			if index == 2 {
				if s1[changeIndex[0]] == s2[changeIndex[1]] && s1[changeIndex[1]] == s2[changeIndex[0]] {
					try = true
				} else {
					return false
				}
			}
		}
	}
	if try || (!try && index == 0) {
		return true
	}
	return false

}

// @lc code=end
