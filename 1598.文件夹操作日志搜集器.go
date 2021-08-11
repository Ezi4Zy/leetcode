/*
 * @lc app=leetcode.cn id=1598 lang=golang
 *
 * [1598] 文件夹操作日志搜集器
 */

// @lc code=start
package main

func minOperations(logs []string) int {
	ret := 0
	for i := 0; i < len(logs); i++ {
		if logs[i] == "../" {
			if ret > 0 {
				ret--
			}
		} else if logs[i] != "./" {
			ret++
		}
	}
	return ret

}

// func main() {
// fmt.Println(minOperations([]string{"d1/", "d2/", "../", "d21/", "./"}))
// fmt.Println(minOperations([]string{"d1/", "d2/", "./", "d3/", "../", "d31/"}))
// fmt.Println(minOperations([]string{"d1/", "../", "../", "../"}))
//
// }

// @lc code=end
