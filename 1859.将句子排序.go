/*
 * @lc app=leetcode.cn id=1859 lang=golang
 *
 * [1859] 将句子排序
 */

// @lc code=start
// package main
//
// import (
// "fmt"
// "strings"
// )

func sortSentence(s string) string {
	words := strings.Split(s, " ")
	ret := make([]string, len(words))
	for i := 0; i < len(words); i++ {
		b := []byte(words[i])
		ret[b[len(b)-1]-'1'] = string(b[:len(b)-1])
	}
	return strings.Join(ret, " ")

}

// func main() {
// s := "is2 sentence4 This1 a3"
// fmt.Println(sortSentence(s))
// }

// @lc code=end
