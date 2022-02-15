/*
 * @lc app=leetcode.cn id=929 lang=golang
 *
 * [929] 独特的电子邮件地址
 */
package main

import (
	"strings"
)

// @lc code=start
func numUniqueEmails(emails []string) int {
	emailMap := make(map[string]bool)
	for i := 0; i < len(emails); i++ {
		email := strings.Split(emails[i], "@")
		index := strings.Index(email[0], "+")
		if index != -1 {
			email[0] = email[0][:index]
		}
		email[0] = strings.ReplaceAll(email[0], ".", "")
		emailMap[email[0]+"@"+email[1]] = true
	}
	return len(emailMap)
}

// func main() {
// fmt.Println(numUniqueEmails([]string{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}),
// numUniqueEmails([]string{"a@leetcode.com", "b@leetcode.com", "c@leetcode.com"}))
// }

// @lc code=end
