/*
 * @lc app=leetcode.cn id=1175 lang=golang
 *
 * [1175] 质数排列
 */
package main

// @lc code=start

var mod = 1000000007

func numPrimeArrangements(n int) int {
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
	primeCount := 0
	for i := 0; i < len(primes); i++ {
		if primes[i] <= n {
			primeCount++
		}
	}
	return (factorial(primeCount) * factorial(n-primeCount)) % mod
}

func factorial(x int) int {
	ret := 1
	for i := 1; i < x+1; i++ {
		ret = (ret * i) % mod
	}
	return ret
}

// func main() {
// fmt.Println(numPrimeArrangements(5), numPrimeArrangements(100))
// }

// @lc code=end
