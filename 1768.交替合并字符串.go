/*
 * @lc app=leetcode.cn id=1768 lang=golang
 *
 * [1768] 交替合并字符串
 */

// @lc code=start
package main

func mergeAlternately(word1 string, word2 string) string {
	b := []byte{}
	index := 0
	for index < len(word1) && index < len(word2) {
		b = append(b, word1[index], word2[index])
		index++
	}
	if index < len(word1) {
		b = append(b, word1[index:]...)

	}
	if index < len(word2) {
		b = append(b, word2[index:]...)
	}
	return string(b)

}

// @lc code=end
