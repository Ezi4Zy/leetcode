/*
 * @lc app=leetcode.cn id=1945 lang=golang
 *
 * [1945] 字符串转化后的各位数字之和
 */
package main

// @lc code=start
func getLucky(s string, k int) int {
	ret := 0
	for i := 0; i < len(s); i++ {
		tmp := int(s[i]-'a') + 1
		ret += tmp%10 + tmp/10
	}
	for i := 1; i < k; i++ {
		temp := 0
		for ret > 0 {
			temp += ret % 10
			ret /= 10
		}
		ret = temp

	}
	return ret
}

// func main() {
// fmt.Println(getLucky("iiii", 1), getLucky("leetcode", 2), getLucky("fleyctuuajsr", 5))
// }

// @lc code=end
