/*
 * @lc app=leetcode.cn id=1441 lang=golang
 *
 * [1441] 用栈操作构建数组
 */

// @lc code=start
package main

func buildArray(target []int, n int) []string {
	ret := make([]string, 0)
	cur := 1
	for i := 0; i < len(target); i++ {
		for cur < target[i] {
			ret = append(ret, "Push")
			ret = append(ret, "Pop")
			cur++
		}
		ret = append(ret, "Push")
		cur++
	}
	return ret
}

//
// func main() {
// fmt.Println(buildArray([]int{1, 2}, 4))
// }

// @lc code=end
