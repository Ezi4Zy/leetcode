/*
 * @lc app=leetcode.cn id=1275 lang=golang
 *
 * [1275] 找出井字棋的获胜者
 */
package main

// @lc code=start
func tictactoe(moves [][]int) string {
	board := make([][3]int, 3)
	for i := 0; i < len(moves); i++ {
		board[moves[i][0]][moves[i][1]] = i%2 + 1
	}
	for i := 0; i < 3; i++ {
		if board[i][0] != 0 && board[i][0] == board[i][1] && board[i][1] == board[i][2]{
			if board[i][0] == 1{
				return "A"
			}else {
				return "B"
			}
		}
		if board[0][i] != 0 && board[0][i] == board[1][i] && board[1][i] == board[2][i]{
			if board[0][i] == 1{
				return "A"
			}else {
				return "B"
			}
		}
	}
	if board[0][0] != 0 && board[0][0] == board[1][1] && board[1][1] == board[2][2]{
		if board[1][1] == 1{
			return "A"
		}else {
			return "B"
		}
	}
	if board[0][2] != 0 && board[0][2] == board[1][1] && board[1][1] == board[2][0]{
		if board[1][1] == 1{
			return "A"
		}else {
			return "B"
		}
	}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if board[i][j] == 0{
				return "Pending"
			}
		}
	}
	return "Draw"
}

// @lc code=end
