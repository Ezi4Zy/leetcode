/*
 * @lc app=leetcode.cn id=1560 lang=golang
 *
 * [1560] 圆形赛道上经过次数最多的扇区
 */

// @lc code=start
package main

import (
	"sort"
)

func mostVisited(n int, rounds []int) []int {
	visited := []int{}
	for i := rounds[0]; ; i++ {
		if i%n == 0 {
			visited = append(visited, n)
		} else {
			visited = append(visited, i%n)
		}
		if i%n == rounds[len(rounds)-1]%n {
			break
		}
	}
	sort.Ints(visited)
	return visited
}

// func main() {
// fmt.Println(mostVisited(4, []int{1, 3, 1, 2}))
// fmt.Println(mostVisited(2, []int{2, 1, 2, 1, 2, 1, 2, 1, 2}))
// fmt.Println(mostVisited(7, []int{1, 3, 5, 7}))
// fmt.Println(mostVisited(3, []int{3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 3, 1}))
// }
//
// @lc code=end
