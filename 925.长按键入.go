/*
 * @lc app=leetcode.cn id=925 lang=golang
 *
 * [925] 长按键入
 */
package main

// @lc code=start
func isLongPressedName(name string, typed string) bool {
	nameIndex := 0
	typedIndex := 0
	for typedIndex < len(typed) {
		if nameIndex >= len(name) || name[nameIndex] != typed[typedIndex] {
			if typedIndex > 0 && typed[typedIndex-1] == typed[typedIndex] {
				typedIndex++
			} else {
				return false
			}
		} else {
			nameIndex++
			typedIndex++
		}
	}
	return typedIndex == len(typed) && nameIndex >= len(name)
}

// @lc code=end
