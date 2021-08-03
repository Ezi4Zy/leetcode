/*
 * @lc app=leetcode.cn id=1736 lang=golang
 *
 * [1736] 替换隐藏数字得到的最晚时间
 */

// @lc code=start
package main

func maximumTime(time string) string {
	ret := make([]byte, 5)
	for i := 0; i < len(time); i++ {
		if time[i] == '?' {
			if i == 0 {
				if time[1] != '?' && time[1] >= '4' {
					ret[0] = '1'
				} else {
					ret[0] = '2'
				}
			} else if i == 1 {
				if ret[0] == '2' {
					ret[1] = '3'
				} else {
					ret[1] = '9'
				}
			} else if i == 3 {
				ret[3] = '5'
			} else {
				ret[4] = '9'
			}
		} else {
			ret[i] = time[i]
		}
	}
	return string(ret)
}

// @lc code=end
