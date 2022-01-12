/*
 * @lc app=leetcode.cn id=1313 lang=golang
 *
 * [1313] 解压缩编码列表
 */
package main

// @lc code=start
func decompressRLElist(nums []int) []int {
	ret := []int{}
	for i := 0; i < len(nums)/2; i++ {
		for j := 0; j < nums[i*2]; j++ {
			ret = append(ret, nums[i*2+1])
		}
	}
	return ret
}

// func main() {
// fmt.Println(decompressRLElist([]int{1, 2, 3, 4}))
// }

// @lc code=end
