/*
 * @lc app=leetcode.cn id=824 lang=golang
 *
 * [824] 山羊拉丁文
 */

// @lc code=start
// package leetcode
import "strings"
var charMap = map[byte]bool{
	'a': true,
	'e': true,
	'i': true,
	'o': true,
	'u': true,
	'A': true,
	'E': true,
	'I': true,
	'O': true,
	'U': true,
}

func toGoatLatin(sentence string) string {
	words := strings.Split(sentence, " ")
	result := make([]string, len(words))
	for i, word := range words {
		tmp := []byte(word)
		if _, ok:= charMap[tmp[0]]; ok{
			result[i] = word + "ma"
		}else {
			result[i] = word[1:] + word[0:1] + "ma"
		}
		result[i] = result[i] + strings.Repeat("a", i+1)
	}
	return strings.Join(result, " ")
}
// @lc code=end

