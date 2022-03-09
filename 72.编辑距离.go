/*
 * @lc app=leetcode.cn id=72 lang=golang
 *
 * [72] 编辑距离
 */
package main

// @lc code=start

func min(i, j int) int {
	if i < j {
		return i
	}
	return j
}

func minDistance(word1 string, word2 string) int {
	result := make([][]int, len(word1)+1)
	for i := 0; i < len(result); i++ {
		result[i] = make([]int, len(word2)+1)
		result[i][0] = i
		if i == 0 {
			for j := 0; j < len(word2)+1; j++ {
				result[i][j] = j
			}
		}
	}
	for i := 1; i < len(result); i++ {
		for j := 1; j < len(result[0]); j++ {
			result[i][j] = min(min(result[i-1][j-1], result[i][j-1]), result[i-1][j]) + 1
			if word1[i-1] == word2[j-1] {
				result[i][j] = min(result[i-1][j-1], result[i][j])
			}
		}
	}
	return result[len(word1)][len(word2)]
}

// func main() {
// fmt.Println(minDistance("horse", "ros"))
// fmt.Println(minDistance("intention", "execution"))
// }

// @lc code=end
