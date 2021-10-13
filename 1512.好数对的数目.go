/*
 * @lc app=leetcode.cn id=1512 lang=golang
 *
 * [1512] 好数对的数目
 */

// @lc code=start
package main

func numIdenticalPairs(nums []int) int {
	count := make(map[int]int)
	ret := 0
	for i := 0; i < len(nums); i++ {
		count[nums[i]] += 1
	}
	for _, v := range count {
		if v >= 2 {
			ret += v * (v - 1) / 2
		}
	}
	return ret
}

// func main() {
// fmt.Println(numIdenticalPairs([]int{1, 2, 3, 1, 1, 3}))
// fmt.Println(numIdenticalPairs([]int{1, 1, 1, 1}))
// fmt.Println(numIdenticalPairs([]int{1, 2, 3}))
// }

// @lc code=end
