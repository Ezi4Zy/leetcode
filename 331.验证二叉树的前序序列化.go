/*
 * @lc app=leetcode.cn id=331 lang=golang
 *
 * [331] 验证二叉树的前序序列化
 */

// @lc code=start
// package leetcode

func isValidSerialization(preorder string) bool {
	slots := 1
	index := 0
	n := len(preorder)
	for index < n {
		if slots == 0 {
			return false
		}
		if preorder[index] == ',' {
			index++
		} else if preorder[index] == '#' {
			slots--
			index++
		} else {
			for index < n && preorder[index] != ',' {
				index++
			}
			slots++
		}
	}
	return slots == 0

}

// @lc code=end
