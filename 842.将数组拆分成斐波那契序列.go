/*
 * @lc app=leetcode.cn id=842 lang=golang
 *
 * [842] 将数组拆分成斐波那契序列
 */
package main

import (
	"math"
)

// @lc code=start
func splitIntoFibonacci(num string) []int {
	ret := []int{}
	var backtrack func(index, sum, pre int) bool
	backtrack = func(index, sum, pre int) bool {
		if index == len(num) {
			return len(ret) >= 3
		}
		cur := 0
		for i := index; i < len(num); i++ {
			if i > index && num[index] == '0' {
				break
			}
			cur = cur*10 + int(num[i]-'0')
			if cur > math.MaxInt32 {
				break
			}
			if len(ret) >= 2 {
				if cur < sum {
					continue
				}
				if cur > sum {
					break
				}
			}
			ret = append(ret, cur)
			if backtrack(i+1, pre+cur, cur) {
				return true
			}
			ret = ret[:len(ret)-1]
		}
		return false
	}
	backtrack(0, 0, 0)
	return ret
}

// func main() {
// fmt.Println(splitIntoFibonacci("1101111"))
// fmt.Println(splitIntoFibonacci("112358130"))
// }

// @lc code=end
