/*
 * @lc app=leetcode.cn id=375 lang=golang
 *
 * [375] 猜数字大小 II
 */
package main

// @lc code=start
func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
func getMoneyAmount(n int) int {
	f := make([][]int, n+1)
	for i := 0; i < len(f); i++ {
		f[i] = make([]int, n+1)
	}
	for i := n - 1; i > 0; i-- {
		for j := i + 1; j < n+1; j++ {
			f[i][j] = j + f[i][j-1]
			for k := i; k < j; k++ {
				cost := k + max(f[i][k-1], f[k+1][j])
				if cost < f[i][j] {
					f[i][j] = cost
				}
			}
		}
	}
	return f[1][n]

}

// func main() {
// fmt.Println(getMoneyAmount(10))
// fmt.Println(getMoneyAmount(1))
// fmt.Println(getMoneyAmount(2))
// fmt.Println(getMoneyAmount(25))
// fmt.Println(getMoneyAmount(5))
// }

// @lc code=end
