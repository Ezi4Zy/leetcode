/*
 * @lc app=leetcode.cn id=1869 lang=golang
 *
 * [1869] 哪种连续子字符串更长
 */

// @lc code=start
// package leetcode

func checkZeroOnes(s string) bool {
	lenOne := 0
	lenZero := 0
	lenCur := 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			lenCur += 1
		} else {
			if s[i-1] == '0' {
				if lenCur > lenZero {
					lenZero = lenCur
				}
			} else {
				if lenCur > lenOne {
					lenOne = lenCur
				}
			}
			lenCur = 1
		}
	}
	if s[len(s)-1] == '0' {
		if lenCur > lenZero {
			lenZero = lenCur
		}
	} else {
		if lenCur > lenOne {
			lenOne = lenCur
		}
	}
	return lenOne > lenZero

}

// @lc code=end
