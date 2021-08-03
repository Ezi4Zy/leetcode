/*
 * @lc app=leetcode.cn id=1742 lang=golang
 *
 * [1742] 盒子中小球的最大数量
 */

// @lc code=start
package main

func countBalls(lowLimit int, highLimit int) int {
	box := make(map[int]int)
	for i := lowLimit; i < highLimit+1; i++ {
		j := i
		sum := 0
		for j > 0 {
			sum += j % 10
			j /= 10
		}
		box[sum]++
	}
	count := 0
	for _, v := range box {
		if v > count {
			count = v
		}
	}
	return count
}

// func main() {
// fmt.Println(countBalls(1, 10))
// fmt.Println(countBalls(5, 15))
// fmt.Println(countBalls(19, 28))
// }
//
// @lc code=end
