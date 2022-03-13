/*
 * @lc app=leetcode.cn id=128 lang=golang
 *
 * [128] 最长连续序列
 */
package main

// @lc code=start
func longestConsecutive(nums []int) int {
	consecutiveLengthMap := make(map[int]int)
	ret := 0
	for i := 0; i < len(nums); i++ {
		if consecutiveLengthMap[nums[i]] == 0 {
			left := consecutiveLengthMap[nums[i]-1]
			right := consecutiveLengthMap[nums[i]+1]
			consecutiveLengthMap[nums[i]] = left + right + 1
			if consecutiveLengthMap[nums[i]] > ret {
				ret = consecutiveLengthMap[nums[i]]
			}
			consecutiveLengthMap[nums[i]-left] = consecutiveLengthMap[nums[i]]
			consecutiveLengthMap[nums[i]+right] = consecutiveLengthMap[nums[i]]
		}
	}
	return ret
}

// func main() {
// fmt.Println(longestConsecutive([]int{100, 4, 200, 1, 3, 2}))
// fmt.Println(longestConsecutive([]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}))
// }

// @lc code=end
