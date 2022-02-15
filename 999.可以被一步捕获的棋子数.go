/*
 * @lc app=leetcode.cn id=999 lang=golang
 *
 * [999] 可以被一步捕获的棋子数
 */
package main

// @lc code=start
func numRookCaptures(board [][]byte) int {
	var rookX, rookY int
	for i := 0; i < len(board); i++ {
		flag := false
		for j := 0; j < len(board[0]); j++ {
			if board[i][j] == 'R' {
				rookX, rookY = i, j
				flag = true
				break
			}
		}
		if flag {
			break
		}
	}
	pawnCount := 0
	i := rookX - 1
	for i >= 0 {
		flag := false
		switch board[i][rookY] {
		case '.':
			i--
		case 'B':
			flag = true
		case 'p':
			pawnCount++
			flag = true
		}
		if flag {
			break
		}
	}
	i = rookX + 1
	for i < len(board) {
		flag := false
		switch board[i][rookY] {
		case '.':
			i++
		case 'B':
			flag = true
		case 'p':
			pawnCount++
			flag = true
		}
		if flag {
			break
		}
	}
	j := rookY - 1
	for j >= 0 {
		flag := false
		switch board[rookX][j] {
		case '.':
			j--
		case 'B':
			flag = true
		case 'p':
			pawnCount++
			flag = true
		}
		if flag {
			break
		}
	}
	j = rookY + 1
	for j < len(board[0]) {
		flag := false
		switch board[rookX][j] {
		case '.':
			j++
		case 'B':
			flag = true
		case 'p':
			pawnCount++
			flag = true
		}
		if flag {
			break
		}
	}
	return pawnCount
}

// func main() {
// fmt.Println(numRookCaptures([][]byte{
// {'.', '.', '.', '.', '.', '.', '.', '.'},
// {'.', '.', '.', 'p', '.', '.', '.', '.'},
// {'.', '.', '.', 'R', '.', '.', '.', 'p'},
// {'.', '.', '.', '.', '.', '.', '.', '.'},
// {'.', '.', '.', '.', '.', '.', '.', '.'},
// {'.', '.', '.', 'p', '.', '.', '.', '.'},
// {'.', '.', '.', '.', '.', '.', '.', '.'},
// {'.', '.', '.', '.', '.', '.', '.', '.'},
// }))
// }

// @lc code=end
