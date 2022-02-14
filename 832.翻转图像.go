/*
 * @lc app=leetcode.cn id=832 lang=golang
 *
 * [832] 翻转图像
 */
package main

// @lc code=start
func flipAndInvertImage(image [][]int) [][]int {
	for i := 0; i < len(image); i++ {
		for j := 0; j < len(image[i])/2; j++ {
			image[i][j], image[i][len(image[i])-j-1] = image[i][len(image[i])-j-1], image[i][j]
		}
		for j := 0; j < len(image[i]); j++ {
			image[i][j] = (image[i][j] + 1) % 2
		}
	}
	return image
}

// func main() {
// fmt.Println(flipAndInvertImage([][]int{
// {1, 1, 0},
// {1, 0, 1},
// {0, 0, 0},
// }))
// }

// @lc code=end
