/*
 * @lc app=leetcode.cn id=1189 lang=golang
 *
 * [1189] “气球” 的最大数量
 */
package main

// @lc code=start
func maxNumberOfBalloons(text string) int {
	cost := map[byte]int{
		'b': 1,
		'a': 1,
		'l': 2,
		'o': 2,
		'n': 1,
	}
	counter := make(map[byte]int)
	for i := 0; i < len(text); i++ {
		if cost[text[i]] > 0 {
			counter[text[i]]++
		}
	}
	count := counter['b'] / cost['b']
	for b, c := range cost {
		if counter[b]/c < count {
			count = counter[b] / c
		}
	}
	return count
}

// func main() {
// fmt.Println(maxNumberOfBalloons("nlaebolko"))
// fmt.Println(maxNumberOfBalloons("loonbalxballpoon"))
// fmt.Println(maxNumberOfBalloons("leetcode"))
// }

// @lc code=end
