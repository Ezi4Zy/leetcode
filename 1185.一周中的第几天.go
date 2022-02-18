/*
 * @lc app=leetcode.cn id=1185 lang=golang
 *
 * [1185] 一周中的第几天
 */
package main

import (
	"time"
)

// @lc code=start
func dayOfTheWeek(day int, month int, year int) string {
	t := time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.Now().Location())
	return t.Weekday().String()
}

// func main() {
// fmt.Println(dayOfTheWeek(31, 8, 2019))
// }

// @lc code=end
