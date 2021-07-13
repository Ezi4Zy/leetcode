/*
 * @lc app=leetcode.cn id=804 lang=golang
 *
 * [804] 唯一摩尔斯密码词
 */

// @lc code=start
// package leetcode


func uniqueMorseRepresentations(words []string) int {
	letterMap := [26]string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
	wordsMap := make(map[string]bool)
	for _, word := range words {
		s := ""
		for i := 0; i < len(word); i++ {
			s += letterMap[word[i]-'a']
		}
		wordsMap[s] = true
	}
	return len(wordsMap)

}
// @lc code=end

