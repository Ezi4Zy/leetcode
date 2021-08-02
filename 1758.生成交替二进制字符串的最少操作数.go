/*
 * @lc app=leetcode.cn id=1758 lang=golang
 *
 * [1758] 生成交替二进制字符串的最少操作数
 */

// @lc code=start
package main

func minOperations(s string) int {
	count0, count1 := 0, 0
	for i := 0; i < len(s); i++ {
		if i%2 == 0 {
			if s[i] == '1' {
				count0++
			} else {
				count1++
			}
		} else {
			if s[i] == '0' {
				count0++
			} else {
				count1++
			}
		}
	}
	if count0 > count1 {
		return count1
	} else {
		return count0
	}

}

//
// func main() {
// fmt.Println(minOperations("0100"))
// }
//
// @lc code=end
