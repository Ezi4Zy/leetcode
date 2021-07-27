/*
 * @lc app=leetcode.cn id=1773 lang=golang
 *
 * [1773] 统计匹配检索规则的物品数量
 */

// @lc code=start
// package leetcode

func countMatches(items [][]string, ruleKey string, ruleValue string) int {
	var index int
	switch ruleKey {
	case "type":
		index = 0
	case "color":
		index = 1
	case "name":
		index = 2
	default:
		index = 0
	}
	ret := 0
	for _, item := range items {
		if item[index] == ruleValue {
			ret++
		}
	}
	return ret
}

// @lc code=end
