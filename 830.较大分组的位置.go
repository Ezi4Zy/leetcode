/*
 * @lc app=leetcode.cn id=830 lang=golang
 *
 * [830] 较大分组的位置
 */
package main

// @lc code=start
func largeGroupPositions(s string) [][]int {
	ret := [][]int{}
	for start := 0; start < len(s); {
		end := start + 1
		for end < len(s) && s[end] == s[start] {
			end++
		}
		if end-start >= 3 {
			ret = append(ret, []int{start, end - 1})
		}
		start = end
	}
	return ret
}

// func main(){
// fmt.Println(largeGroupPositions("abbxxxxzzy"))
// }

// @lc code=end
