/*
 * @lc app=leetcode.cn id=1854 lang=golang
 *
 * [1854] 人口最多的年份
 */

// @lc code=start
// package main
//
// import "fmt"

func maximumPopulation(logs [][]int) int {
	ret := make(map[int]int)
	for _, log := range logs {
		for i := log[0]; i < log[1]; i++ {
			ret[i]++
		}
	}
	ans := 1950
	birth := 0
	for k, v := range ret {
		if v > birth || (v == birth && k < ans) {
			birth = v
			ans = k
		}
	}
	return ans
}

// func main() {
// fmt.Println(maximumPopulation([][]int{}))
// var p [][]int
// p = append(p, []int{1993, 1999})
// p = append(p, []int{2000, 2010})
// fmt.Println(maximumPopulation(p))
// }

// @lc code=end
