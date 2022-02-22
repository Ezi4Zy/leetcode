/*
 * @lc app=leetcode.cn id=1952 lang=golang
 *
 * [1952] 三除数
 */
package main

// @lc code=start
func isThree(n int) bool {
	count := 0
	for i := 1; i*i <= n; i++ {
		if n%i == 0 {
			if i != n/i {
				count += 2
			} else {
				count += 1
			}
		}
	}
	return count == 3
}

// func main() {
// fmt.Println(isThree(2), isThree(4))
// }

// @lc code=end
