/*
 * @lc app=leetcode.cn id=200 lang=golang
 *
 * [200] 岛屿数量
 */

package main

// @lc code=start

func change(i int, j int, grid [][]byte) {
	flag := 0
	if i > 0 && grid[i-1][j] == '1' {
		flag += 1
		grid[i-1][j] = '2'
	}
	if i < len(grid)-1 && grid[i+1][j] == '1' {
		flag += 2
		grid[i+1][j] = '2'
	}
	if j > 0 && grid[i][j-1] == '1' {
		flag += 4
		grid[i][j-1] = '2'
	}
	if j < len(grid[i])-1 && grid[i][j+1] == '1' {
		flag += 8
		grid[i][j+1] = '2'
	}
	if flag&1 == 1 {
		change(i-1, j, grid)
	}
	if flag&2 == 2 {
		change(i+1, j, grid)
	}
	if flag&4 == 4 {
		change(i, j-1, grid)
	}
	if flag&8 == 8 {
		change(i, j+1, grid)
	}
}

// func printIsland(grid [][]byte) {
// for i := 0; i < len(grid); i++ {
// fmt.Println(string(grid[i]))
// }
// }

func numIslands(grid [][]byte) int {
	count := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' {
				count++
				grid[i][j] = '2'
				change(i, j, grid)
			}
		}
	}
	return count
}

// func main() {
// fmt.Println(numIslands([][]byte{
// {'1', '1', '1', '1', '0'},
// {'1', '1', '0', '1', '0'},
// {'1', '1', '0', '0', '0'},
// {'0', '0', '0', '0', '0'},
// }))
// fmt.Println(numIslands([][]byte{
// {'1', '1', '0', '0', '0'},
// {'1', '1', '0', '0', '0'},
// {'0', '0', '1', '0', '0'},
// {'0', '0', '0', '1', '1'},
// }))
// }

// @lc code=end
