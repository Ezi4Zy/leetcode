/*
 * @lc app=leetcode.cn id=1832 lang=golang
 *
 * [1832] 判断句子是否为全字母句
 */

// @lc code=start
// package main
//
// import "fmt"

func checkIfPangram(sentence string) bool {
	ret := 0
	for i := 0; i < len(sentence); i++ {
		ret |= 1 << (sentence[i] - 'a')
	}
	return ret == 1<<26-1
}

// func main() {
// fmt.Println(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
// fmt.Println(checkIfPangram("leetcode"))
// }

// @lc code=end
