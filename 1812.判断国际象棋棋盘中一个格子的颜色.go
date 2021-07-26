/*
 * @lc app=leetcode.cn id=1812 lang=golang
 *
 * [1812] 判断国际象棋棋盘中一个格子的颜色
 */

// @lc code=start
// package main
//
// import "fmt"

func squareIsWhite(coordinates string) bool {
	return (coordinates[0]-'a')%2 != (coordinates[1]-'1')%2
}

// func main() {
// fmt.Println(squareIsWhite("a1"))
// fmt.Println(squareIsWhite("h3"))
// fmt.Println(squareIsWhite("c7"))
// fmt.Println(squareIsWhite("h8"))
// }

// @lc code=end
