/*
 * @lc app=leetcode.cn id=914 lang=golang
 *
 * [914] 卡牌分组
 */
package main

// @lc code=start
func hasGroupsSizeX(deck []int) bool {
	counter := make(map[int]int)
	for i := 0; i < len(deck); i++ {
		counter[deck[i]]++
	}
	minCount := len(deck)
	for _, count := range counter {
		if count < minCount {
			minCount = count
		}
	}
	if minCount < 2 {
		return false
	}
	for i := 2; i < minCount+1; i++ {
		if minCount%i == 0 {
			flag := true
			for _, count := range counter {
				if count%i != 0 {
					flag = false
					break
				}
			}
			if flag {
				return flag
			}
		}
	}
	return false
}

// func main() {
// fmt.Println(hasGroupsSizeX([]int{1, 1, 2, 2, 3, 3, 4, 4}),
// hasGroupsSizeX([]int{1, 1, 1, 2, 2, 2, 3, 3}),
// hasGroupsSizeX([]int{1, 1, 1, 1, 2, 2, 3, 3}))
// }

// @lc code=end
