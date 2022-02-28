/*
 * @lc app=leetcode.cn id=423 lang=golang
 *
 * [423] 从英文中重建数字
 */
package main

import (
	"bytes"
)

// @lc code=start

func originalDigits(s string) string {
	counter := make([]int, 10)
	letterCounter := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		letterCounter[s[i]]++
	}
	numWords := []map[byte]int{
		{'z': 1, 'e': 1, 'r': 1, 'o': 1},
		{'o': 1, 'n': 1, 'e': 1},
		{'t': 1, 'w': 1, 'o': 1},
		{'t': 1, 'h': 1, 'r': 1, 'e': 2},
		{'f': 1, 'o': 1, 'u': 1, 'r': 1},
		{'f': 1, 'i': 1, 'v': 1, 'e': 1},
		{'s': 1, 'i': 1, 'x': 1},
		{'s': 1, 'e': 2, 'v': 1, 'n': 1},
		{'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1},
		{'n': 2, 'i': 1, 'e': 1},
	}
	specialLettersMap := map[byte]byte{'z': 0, 'w': 2, 'x': 6, 'g': 8, 'u': 4, 'f': 5, 'h': 3, 'v': 7, 'i': 9, 'n': 1}
	specialLetters := []byte{'z', 'w', 'x', 'g', 'u', 'f', 'h', 'v', 'i', 'n'}
	for _, b := range specialLetters {
		i := specialLettersMap[b]
		// fmt.Println(string(b), specialLettersMap[b], letterCounter[b])
		if letterCounter[b] != 0 {
			count := letterCounter[b] / numWords[i][b]
			counter[i] = count
			for wb, c := range numWords[i] {
				letterCounter[wb] -= count * c
			}
		}
	}
	ret := []byte{}
	for i := 0; i < len(counter); i++ {
		ret = append(ret, bytes.Repeat([]byte{byte('0' + i)}, counter[i])...)
	}
	return string(ret)
}

// func main() {
// fmt.Println(originalDigits("owoztneoer"))
// fmt.Println(originalDigits("fviefuro"))
// }

// @lc code=end
