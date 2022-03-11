/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */
package main

// @lc code=start
func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}
func min(i, j int) int {
	if i < j {
		return i
	}
	return j
}
func trap(height []int) int {
	water := 0
	left := 0
	right := len(height) - 1
	leftMax := 0
	rightMax := 0
	for left < right {
		leftMax = max(height[left], leftMax)
		rightMax = max(height[right], rightMax)
		if leftMax < rightMax {
			water += leftMax - height[left]
			left++
		} else {
			water += rightMax - height[right]
			right--
		}
	}
	return water
}
func trap2(height []int) int {
	leftMax := make([]int, len(height))
	rightMax := make([]int, len(height))
	leftMax[0] = height[0]
	rightMax[len(height)-1] = height[len(height)-1]
	for i := 1; i < len(height); i++ {
		leftMax[i] = max(leftMax[i-1], height[i])
	}
	for i := len(height) - 2; i >= 0; i-- {
		rightMax[i] = max(rightMax[i+1], height[i])
	}
	water := 0
	for i := 1; i < len(height)-1; i++ {
		water += min(leftMax[i], rightMax[i]) - height[i]
	}
	return water
}
func trap1(height []int) int {
	start := 0
	end := start + 1
	water := 0
	stones := 0
	for start < len(height)-1 {
		if end < len(height) && height[end] >= height[start] {
			water += height[start]*(end-start-1) - stones
			stones = 0
			start = end
			end++
		} else {
			if end == len(height) {
				for start < len(height)-1 {
					index := start + 2
					hIndex := start + 1
					hStones := 0
					stones = height[hIndex]
					for index < len(height) {
						if height[index] >= height[hIndex] {
							hIndex = index
							hStones = stones
						}
						stones += height[index]
						index++
					}
					water += height[hIndex]*(hIndex-start-1) - hStones
					start = hIndex
				}

			} else {
				stones += height[end]
				end++
			}
		}
	}
	return water
}

// func main() {
// fmt.Println(trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
// fmt.Println(trap([]int{4, 2, 0, 3, 2, 5}))
// fmt.Println(trap([]int{4, 2, 3}))
// }

// @lc code=end
