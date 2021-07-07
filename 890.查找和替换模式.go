/*
 * @lc app=leetcode.cn id=890 lang=golang
 *
 * [890] 查找和替换模式
 */

// @lc code=start
// package leetcode

func findAndReplacePattern(words []string, pattern string) []string {
	bytesPattern := []byte(pattern)
	res := []string{}
	for _, word := range words {
		wpMap := make(map[byte]byte)
		pwMap := make(map[byte]byte)
		bytes := []byte(word)
		flag := true
		for i, b := range bytes {
			if pb, ok := wpMap[b]; ok {
				if pb != bytesPattern[i] {
					flag = false
					break
				}
			} else {
				if _, ok := pwMap[bytesPattern[i]]; ok {
					flag = false
					break
				} else {
					wpMap[b] = bytesPattern[i]
					pwMap[bytesPattern[i]] = b
				}
			}
		}
		if flag {
			res = append(res, word)
		}
	}
	return res
}

// @lc code=end
