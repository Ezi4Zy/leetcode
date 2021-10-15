/*
 * @lc app=leetcode.cn id=1417 lang=golang
 *
 * [1417] 重新格式化字符串
 */

// @lc code=start
package main

import (
	"unicode"
)

func reformat(s string) string {
	ret := []byte{}
	number := 0
	letter := 0
	length := len(s)
	numberCount := 0
	for i := 0; i < length; i++ {
		if unicode.IsNumber(rune(s[i])) {
			numberCount++
		}
	}
	signal := true
	if numberCount*2 < length {
		signal = false
	}
	for {
		if signal {
			if number == length {
				break
			}
			if unicode.IsNumber(rune(s[number])) {
				ret = append(ret, s[number])
				number++
				signal = false
			} else {
				number++
			}
		} else {
			if letter == length {
				break
			}
			if unicode.IsLower(rune(s[letter])) {
				ret = append(ret, s[letter])
				letter++
				signal = true
			} else {
				letter++
			}
		}
	}
	if len(ret) != length {
		return ""
	}
	return string(ret)

}

// func main() {
// fmt.Println(reformat("a0b1c2"))
// fmt.Println(reformat("leetcode"))
// fmt.Println(reformat("123456789"))
// fmt.Println(reformat("covid2019"))
// }

// @lc code=end
