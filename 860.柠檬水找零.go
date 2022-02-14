/*
 * @lc app=leetcode.cn id=860 lang=golang
 *
 * [860] 柠檬水找零
 */
package main

// @lc code=start
func lemonadeChange(bills []int) bool {
	cashes := [2]int{}
	for i := 0; i < len(bills); i++ {
		if bills[i] == 5 {
			cashes[0]++
		}
		if bills[i] == 10 {
			if cashes[0] == 0 {
				return false
			} else {
				cashes[0]--
				cashes[1]++
			}
		}
		if bills[i] == 20 {
			if cashes[1] > 0 {
				if cashes[0] > 0 {
					cashes[0]--
					cashes[1]--
				} else {
					return false
				}
			} else {
				if cashes[0] > 2 {
					cashes[0] -= 3
				} else {
					return false
				}
			}
		}
	}
	return true
}

// func main() {
// fmt.Println(lemonadeChange([]int{5, 5, 5, 10, 20}),
// lemonadeChange([]int{5, 5, 10, 10, 20}),
// lemonadeChange([]int{5, 5, 10}),
// lemonadeChange([]int{10, 10}))
// }

// @lc code=end
