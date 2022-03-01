/*
 * @lc app=leetcode.cn id=1387 lang=golang
 *
 * [1387] 将整数按权重排序
 */
package main

import (
	"sort"
)

// @lc code=start

type Weight struct {
	Val  int
	Step int
}

var stepMap = map[int]int{
	0: 1,
	1: 0,
	2: 1,
}

func caculateStep(val int) int {
	if step, ok := stepMap[val]; ok {
		return step
	} else {
		if val%2 == 0 {
			stepMap[val] = 1 + caculateStep(val/2)
		} else {
			stepMap[val] = 1 + caculateStep(val*3+1)
		}
		return stepMap[val]
	}
}

func getKth(lo int, hi int, k int) int {
	var weights = make([]Weight, hi-lo+1)
	for i := lo; i <= hi; i++ {
		step := caculateStep(i)
		weights[i-lo] = Weight{
			Val:  i,
			Step: step,
		}
	}
	sort.Slice(weights, func(i, j int) bool {
		if weights[i].Step == weights[j].Step {
			return weights[i].Val < weights[j].Val
		}
		return weights[i].Step < weights[j].Step
	})
	return weights[k-1].Val
}

// func main() {
// fmt.Println(getKth(12, 15, 2))
// fmt.Println(getKth(1, 1, 1))
// fmt.Println(getKth(7, 11, 4))
// fmt.Println(getKth(10, 20, 5))
// fmt.Println(getKth(1, 1000, 777))
// }

// @lc code=end
