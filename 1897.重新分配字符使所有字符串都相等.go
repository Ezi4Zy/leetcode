/*
 * @lc app=leetcode.cn id=1897 lang=golang
 *
 * [1897] 重新分配字符使所有字符串都相等
 */

// @lc code=start
// package leetcode

func makeEqual(words []string) bool {
	length := len(words)
	byteMap := make(map[byte]int)
	for i := 0; i < length; i++ {
		for j := 0; j < len(words[i]); j++ {
			byteMap[words[i][j]]++
		}
	}
	for _, v := range byteMap {
		if v%length != 0 {
			return false
		}
	}
	return true
}

// @lc code=end
