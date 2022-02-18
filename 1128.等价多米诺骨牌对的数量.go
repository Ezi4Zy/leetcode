/*
 * @lc app=leetcode.cn id=1128 lang=golang
 *
 * [1128] 等价多米诺骨牌对的数量
 */
package main

// @lc code=start
func numEquivDominoPairs(dominoes [][]int) int {
	counter := make([]int, 100)
	count := 0
	for i := 0; i < len(dominoes); i++ {
		val := 0
		if dominoes[i][0] > dominoes[i][1] {
			val = dominoes[i][0]*10 + dominoes[i][1]
		} else {
			val = dominoes[i][1]*10 + dominoes[i][0]
		}
		count += counter[val]
		counter[val]++
	}
	return count
}

// func main() {
// fmt.Println(numEquivDominoPairs([][]int{
// {1, 2},
// {2, 1},
// {3, 4},
// {5, 6},
// }))
// }

// @lc code=end
