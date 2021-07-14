/*
 * @lc app=leetcode.cn id=1507 lang=golang
 *
 * [1507] 转变日期格式
 */

// @lc code=start
// package leetcode

import "strings"

func reformatDate(date string) string {
	monthMap := map[string]string{
		"Jan": "01",
		"Feb": "02",
		"Mar": "03",
		"Apr": "04",
		"May": "05",
		"Jun": "06",
		"Jul": "07",
		"Aug": "08",
		"Sep": "09",
		"Oct": "10",
		"Nov": "11",
		"Dec": "12",
	}
	d := strings.Split(date, " ")
	var day string
	if len(d[0]) == 3 {
		day = "0" + d[0][0:1]
	} else {
		day = d[0][0:2]
	}

	return d[2] + "-" + monthMap[d[1]] + "-" + day

}

// @lc code=end
