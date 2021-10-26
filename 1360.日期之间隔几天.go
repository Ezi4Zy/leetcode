/*
 * @lc app=leetcode.cn id=1360 lang=golang
 *
 * [1360] 日期之间隔几天
 */

// @lc code=start
package main

import (
	"math"
	"strconv"
	"strings"
)

func dateToDays(date string) int {
	dateSlice := strings.Split(date, "-")
	year, _ := strconv.Atoi(dateSlice[0])
	month, _ := strconv.Atoi(dateSlice[1])
	day, _ := strconv.Atoi(dateSlice[2])
	monthDays := []int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	days := day - 1
	for month != 0 {
		month--
		days += monthDays[month]
		if month == 2 && (year%400 == 0 || (year%4 == 0 && year%100 != 0)) {
			days++
		}
	}
	days += 365 * (year - 1971)
	days += (year-1)/4 - 1971/4
	days -= (year-1)/100 - 1971/100
	days += (year-1)/400 - 1971/400
	return days
}
func daysBetweenDates(date1 string, date2 string) int {
	return int(math.Abs(float64(dateToDays(date1)) - float64(dateToDays(date2))))
}

// @lc code=end
