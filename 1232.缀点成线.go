/*
 * @lc app=leetcode.cn id=1232 lang=golang
 *
 * [1232] 缀点成线
 */
package main

// @lc code=start
func checkStraightLine(coordinates [][]int) bool {
	for i := 2; i < len(coordinates); i++ {
		if (coordinates[i-1][0]-coordinates[i-2][0])*(coordinates[i][1]-coordinates[i-1][1]) != (coordinates[i][0]-coordinates[i-1][0])*(coordinates[i-1][1]-coordinates[i-2][1]) {
			return false
		}
	}
	return true
}

// func main() {
// fmt.Println(checkStraightLine([][]int{
// {1, 2},
// {2, 3},
// {3, 4},
// {4, 5},
// {5, 6},
// {6, 7},
// }))
// fmt.Println(checkStraightLine([][]int{
// {1, 1},
// {2, 2},
// {3, 4},
// {4, 5},
// {5, 6},
// {7, 7},
// }))
// }

// @lc code=end
