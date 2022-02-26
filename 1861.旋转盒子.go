/*
 * @lc app=leetcode.cn id=1861 lang=golang
 *
 * [1861] 旋转盒子
 */
package main

// @lc code=start
func rotateTheBox(box [][]byte) [][]byte {
	ret := make([][]byte, len(box[0]))
	for i := 0; i < len(ret); i++ {
		ret[i] = make([]byte, len(box))
	}
	for i := 0; i < len(box); i++ {
		flag := true
		for flag {
			flag = false
			for j := len(box[i]) - 1; j > 0; j-- {
				if box[i][j] == '.' && box[i][j-1] == '#' {
					box[i][j] = '#'
					box[i][j-1] = '.'
					flag = true
				}
			}
		}
		for j := 0; j < len(box[i]); j++ {
			ret[j][len(box)-i-1] = box[i][j]
		}
	}
	return ret
}

// func main() {
// ret := rotateTheBox([][]byte{
// {'#', '.', '#'},
// })
// for i := 0; i < len(ret); i++ {
// fmt.Println(string(ret[i]))
// }

// ret = rotateTheBox([][]byte{
// {'#', '#', '*', '.', '*', '.'},
// {'#', '#', '#', '*', '.', '.'},
// {'#', '#', '#', '.', '#', '.'},
// })
// for i := 0; i < len(ret); i++ {
// fmt.Println(string(ret[i]))
// }
// }

// @lc code=end
