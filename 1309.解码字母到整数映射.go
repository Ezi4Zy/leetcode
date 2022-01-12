/*
 * @lc app=leetcode.cn id=1309 lang=golang
 *
 * [1309] 解码字母到整数映射
 */
package main

import (
	"strconv"
)

// @lc code=start
func freqAlphabets(s string) string {
	ret := ""
	for i := 0; i < len(s); {
		if i+2 < len(s) && s[i+2] == '#' {
			diff, _ := strconv.Atoi(s[i : i+2])
			ret += string(rune('j' + diff - 10))
			i += 3
		} else {
			diff, _ := strconv.Atoi(s[i : i+1])
			ret += string(rune('a' + diff - 1))
			i += 1
		}
	}
	return ret
}

// func main()  {
// fmt.Println(freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
// }

// @lc code=end
