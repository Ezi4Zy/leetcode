/*
 * @lc app=leetcode.cn id=762 lang=golang
 *
 * [762] 二进制表示中质数个计算置位
 */
package main

// @lc code=start
func countPrimeSetBits(left int, right int) int {
	primeMap := map[int]bool{
		2:  true,
		3:  true,
		5:  true,
		7:  true,
		11: true,
		13: true,
		17: true,
		19: true,
	}
	primeCount := 0
	for i := left; i < right+1; i++ {
		tmp := i
		count := 0
		for tmp > 0 {
			count += tmp % 2
			tmp /= 2
		}
		if primeMap[count] {
			primeCount++
		}
	}
	return primeCount
}

// func main() {
// fmt.Println(countPrimeSetBits(6, 10))
// fmt.Println(countPrimeSetBits(10, 15))
// }

// @lc code=end
