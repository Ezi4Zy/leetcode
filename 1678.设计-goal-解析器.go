/*
 * @lc app=leetcode.cn id=1678 lang=golang
 *
 * [1678] 设计 Goal 解析器
 */

// @lc code=start
package main

func interpret(command string) string {
	b := []byte{}
	for i := 0; i < len(command); i++ {
		if command[i] == ')' {
			if command[i-1] == '(' {
				b = append(b, 'o')
			}
		} else {
			if command[i] != '(' {
				b = append(b, command[i])
			}
		}
	}
	return string(b)
}

//
// func main() {
// fmt.Println(interpret("G()(al)"))
// fmt.Println(interpret("G()()()()(al)"))
// fmt.Println(interpret("(al)G(al)()()G"))
// }

// @lc code=end
