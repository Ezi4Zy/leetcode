/*
 * @lc app=leetcode.cn id=1646 lang=golang
 *
 * [1646] 获取生成数组中的最大值
 */

// @lc code=start
// package leetcode

func getMaximumGenerated(n int) int {
	ret := make([]int, 0)
	max := 0
	for i := 0; i < n + 1; i++ {
		if i < 2 {
			ret = append(ret, i)
		}else {
			if i % 2 == 0{
				ret = append(ret, ret[i / 2])
			}else {
				ret = append(ret, ret[i/2]+ret[i/2+1])
			}
		}
		if ret[i] > max{
			max = ret[i]
		}
	}
	return max

}
// @lc code=end

