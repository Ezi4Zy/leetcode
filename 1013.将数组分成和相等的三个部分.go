/*
 * @lc app=leetcode.cn id=1013 lang=golang
 *
 * [1013] 将数组分成和相等的三个部分
 */
package main

// @lc code=start
func canThreePartsEqualSum(arr []int) bool {
	sum := 0
	for i := 0; i < len(arr); i++ {
		sum += arr[i]
	}
	if sum%3 != 0 {
		return false
	}
	sum /= 3
	part1 := 0
	part2 := 0
	part3 := 0
	for i := 0; i < len(arr); i++ {
		part1 += arr[i]
		if part1 == sum {
			for j := i + 1; j < len(arr); j++ {
				part2 += arr[j]
				if part2 == sum && j != len(arr)-1 {
					for m := j + 1; m < len(arr); m++ {
						part3 += arr[m]
					}
					if part3 == sum {
						return true
					}
					part3 = 0
				}
			}
			part2 = 0
		}
	}
	return false
}

// func main() {
// fmt.Println(canThreePartsEqualSum([]int{0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1}),
// canThreePartsEqualSum([]int{0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1}),
// canThreePartsEqualSum([]int{3, 3, 6, 5, -2, 2, 5, 1, -9, 4}))
// }

// @lc code=end
