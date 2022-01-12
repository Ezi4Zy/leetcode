/*
 * @lc app=leetcode.cn id=1281 lang=golang
 *
 * [1281] 整数的各位积和之差
 */
package main

// @lc code=start
func subtractProductAndSum(n int) int {
	sum := 0
	product := 1
	for n > 0 {
		sum += n % 10
		product *= n % 10
		n /= 10
	}
	return product - sum
}

// func main() {
// fmt.Println(subtractProductAndSum(234))
// fmt.Println(subtractProductAndSum(4421))
// }

// @lc code=end
