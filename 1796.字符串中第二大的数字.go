/*
 * @lc app=leetcode.cn id=1796 lang=golang
 *
 * [1796] 字符串中第二大的数字
 */

// @lc code=start
// package main
//
// import "fmt"

func secondHighest(s string) int {
	top1, top2 := -1, -1
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			tmp := int(s[i] - '0')
			if tmp > top2 {
				if tmp > top1 {
					top2 = top1
					top1 = tmp
				} else if tmp == top1 {
					continue
				} else {
					top2 = tmp
				}
			}
		}
	}
	return top2

}

//
// func main() {
// fmt.Println(secondHighest("abc1111"))
// }

// @lc code=end
