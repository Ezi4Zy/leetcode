/*
 * @lc app=leetcode.cn id=1880 lang=golang
 *
 * [1880] 检查某单词是否等于两单词之和
 */

// @lc code=start
// package leetcode

func stoi(word string) int {
	ret := 0
	for i := 0; i < len(word); i++ {
		ret += int(word[i] - 'a')
		ret *= 10
	}
	return ret
}

func isSumEqual(firstWord string, secondWord string, targetWord string) bool {
	return stoi(firstWord)+stoi(secondWord) == stoi(targetWord)
}

// @lc code=end
