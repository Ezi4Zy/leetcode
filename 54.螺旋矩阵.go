/*
 * @lc app=leetcode.cn id=54 lang=golang
 *
 * [54] 螺旋矩阵
 */
package main

// @lc code=start
func spiralOrder(matrix [][]int) []int {
	i := 0
	j := 0
	maxI := len(matrix)
	maxJ := len(matrix[0])
	minI := -1
	minJ := -1
	ret := []int{}
	direction := 0
	for i > minI && i < maxI && j > minJ && j < maxJ {
		ret = append(ret, matrix[i][j])
		if direction == 0 {
			j++
			if j == maxJ {
				j--
				i++
				minI++
				direction = (direction + 1) % 4
			}
			continue
		}
		if direction == 1 {
			i++
			if i == maxI {
				i--
				j--
				maxJ--
				direction = (direction + 1) % 4
			}
			continue
		}
		if direction == 2 {
			j--
			if j == minJ {
				i--
				j++
				maxI--
				direction = (direction + 1) % 4
			}
			continue
		}
		if direction == 3 {
			i--
			if i == minI {
				i++
				j++
				minJ++
				direction = (direction + 1) % 4
			}
			continue
		}

	}
	return ret
}

// func main() {
// fmt.Println(spiralOrder([][]int{
// {1, 2, 3, 4},
// {5, 6, 7, 8},
// {9, 10, 11, 12},
// }))
// fmt.Println(spiralOrder([][]int{
// {1, 2, 3},
// {4, 5, 6},
// {7, 8, 9},
// }))
// }

// @lc code=end
