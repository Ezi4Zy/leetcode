/*
 * @lc app=leetcode.cn id=1556 lang=golang
 *
 * [1556] 千位分隔数
 */

// @lc code=start
package main

func thousandSeparator(n int) string {
	ret := make([]byte, 14)
	index := 13
	if n == 0 {
		ret[index] = '0'
		index--
	}
	for n > 0 {
		if (14-index)%4 == 0 {
			ret[index] = '.'
			index--
		} else {
			t := n % 1000
			n /= 1000
			if n == 0 {
				for t > 0 {
					ret[index] = '0' + byte(t%10)
					t /= 10
					index--
				}
			} else {
				for i := 0; i < 3; i++ {
					ret[index] = '0' + byte(t%10)
					t /= 10
					index--
				}
			}

		}

	}
	return string(ret[index+1 : 14])

}

// func main() {
// fmt.Println(thousandSeparator(987),
// thousandSeparator(1234),
// thousandSeparator(123456789),
// thousandSeparator(0),
// thousandSeparator(2147483648),
// thousandSeparator(51040))
// }

// @lc code=end
