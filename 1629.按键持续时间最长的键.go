/*
 * @lc app=leetcode.cn id=1629 lang=golang
 *
 * [1629] 按键持续时间最长的键
 */

// @lc code=start
package main

func slowestKey(releaseTimes []int, keysPressed string) byte {
	index := 0
	slowTime := releaseTimes[0]
	for i := 1; i < len(releaseTimes); i++ {
		if releaseTimes[i]-releaseTimes[i-1] > slowTime {
			index = i
			slowTime = releaseTimes[i] - releaseTimes[i-1]
		} else if releaseTimes[i]-releaseTimes[i-1] == slowTime {
			if keysPressed[i] > keysPressed[index] {
				index = i
			}
		}
	}
	return keysPressed[index]
}

// @lc code=end
