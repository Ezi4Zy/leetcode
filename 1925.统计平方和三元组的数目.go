/*
 * @lc app=leetcode.cn id=1925 lang=golang
 *
 * [1925] 统计平方和三元组的数目
 */
package main

// @lc code=start
func countTriples(n int) int {
	squraMap := make(map[int]bool, n)
	count := 0
	for i := 1; i <= n; i++ {
		squraMap[i*i] = true
	}
	for i := 1; i <= n; i++ {
		for j := i + 1; j <= n; j++ {
			sum := i*i + j*j
			if sum > n*n {
				break
			}
			if squraMap[sum] {
				count += 2
			}
		}
	}

	return count
}

// func main() {
// fmt.Print(countTriples(5), countTriples(10))
// }

// @lc code=end
