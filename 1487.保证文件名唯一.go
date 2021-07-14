/*
 * @lc app=leetcode.cn id=1487 lang=golang
 *
 * [1487] 保证文件名唯一
 */

// @lc code=start
// package leetcode

import (
	"strconv"
)

func getFolderNames(names []string) []string {
	var folderNames []string
	nameMap := make(map[string]int)
	for _, name := range names {
		s := name
		for nameMap[s] > 0{
			s = name + "(" + strconv.Itoa(nameMap[name]) + ")"
			nameMap[name] ++
		}
		nameMap[s] = 1
		folderNames = append(folderNames, s)
	}
	return folderNames

}

// @lc code=end
