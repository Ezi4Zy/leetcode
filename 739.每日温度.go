/*
 * @lc app=leetcode.cn id=739 lang=golang
 *
 * [739] 每日温度
 */

// @lc code=start

// package leetcode

// package leetcode

func dailyTemperatures(temperatures []int) []int {
	stack := []int{}
	ret := make([]int, len(temperatures))
	for i := 0; i < len(temperatures); i++ {
		for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]]{
			ret[stack[len(stack)-1]] = i - stack[len(stack) - 1]
			stack = stack[:len(stack) - 1]
		}
		stack = append(stack, i)
	}
	return ret

}

// @lc code=end

