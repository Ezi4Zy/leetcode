/*
 * @lc app=leetcode.cn id=1374 lang=golang
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */

// @lc code=start
package main

func generateTheString(n int) string {
	ret := make([]byte, n)
	if n%2 == 1 {
		for i := 0; i < n; i++ {
			ret[i] = 'a'
		}
	} else {
		for i := 0; i < n-1; i++ {
			ret[i] = 'a'
		}
		ret[n-1] = 'b'
	}
	return string(ret)
}

// @lc code=end
