/*
 * @lc app=leetcode.cn id=1725 lang=golang
 *
 * [1725] 可以形成最大正方形的矩形数目
 */

// @lc code=start
package main

func countGoodRectangles(rectangles [][]int) int {
	maxLen := 0
	count := 0
	for i := 0; i < len(rectangles); i++ {
		curLen := 0
		if rectangles[i][0] > rectangles[i][1] {
			curLen = rectangles[i][1]
		} else {
			curLen = rectangles[i][0]
		}
		if curLen > maxLen {
			maxLen = curLen
			count = 1
		} else {
			if curLen == maxLen {
				count++
			}
		}

	}
	return count
}

// func main() {
// rectangles := [][]int{}
// rectangles = append(rectangles, []int{5, 8})
// rectangles = append(rectangles, []int{3, 9})
// rectangles = append(rectangles, []int{5, 12})
// rectangles = append(rectangles, []int{16, 5})
// fmt.Println(countGoodRectangles(rectangles))
// }

// @lc code=end
