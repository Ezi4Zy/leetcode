/*
 * @lc app=leetcode.cn id=1979 lang=golang
 *
 * [1979] 找出数组的最大公约数
 */

package main

import "fmt"

// @lc code=start

// gcd求最大公约数
func getGcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func findGCD(nums []int) int {
	minNum := nums[0]
	maxNum := nums[0]
	for _, num := range nums {
		if minNum > num {
			minNum = num
		}
		if maxNum < num {
			maxNum = num
		}
	}
	return getGcd(maxNum, minNum)

}

// @lc code=end

func main() {
	fmt.Println(findGCD([]int{2, 5, 6, 9, 10}))
	fmt.Println(findGCD([]int{7, 5, 6, 8, 3}))
	fmt.Println(findGCD([]int{3, 3}))
}
