/*
 * @lc app=leetcode.cn id=836 lang=golang
 *
 * [836] 矩形重叠
 */
package main

// @lc code=start
func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	return !(rec1[2] <= rec2[0] || rec2[2] <= rec1[0] || rec1[3] <= rec2[1] || rec2[3] <= rec1[1])
}

// func main() {
// fmt.Println(isRectangleOverlap([]int{0, 0, 2, 2}, []int{1, 1, 3, 3}),
// isRectangleOverlap([]int{0, 0, 1, 1}, []int{1, 0, 2, 1}),
// isRectangleOverlap([]int{0, 0, 1, 1}, []int{2, 2, 3, 3}))
// }

// @lc code=end
