/*
 * @lc app=leetcode.cn id=1971 lang=golang
 *
 * [1971] 寻找图中是否存在路径
 */

package main

// @lc code=start

func validPath(n int, edges [][]int, source int, destination int) bool {
	if source == destination {
		return true
	}
	pathes := make(map[int][]int, 0)
	for _, edge := range edges {
		pathes[edge[0]] = append(pathes[edge[0]], edge[1])
		pathes[edge[1]] = append(pathes[edge[1]], edge[0])
	}
	existed := make(map[int]struct{}, 0)
	sources := make(map[int]struct{}, 0)
	sources[source] = struct{}{}
	existed[source] = struct{}{}
	for len(sources) != 0 {
		next := make(map[int]struct{}, 0)
		for source, _ := range sources {
			if sourcePathes, ok := pathes[source]; ok {
				for _, v := range sourcePathes {
					if v == destination {
						return true
					}
					if _, ok := existed[v]; !ok {
						next[v] = struct{}{}
						existed[v] = struct{}{}
					}
				}
			}
		}
		sources = next
	}
	return false
}
// @lc code=end

// func main() {
// fmt.Println(validPath(3, [][]int{
// {0, 1}, {1, 2}, {2, 0},
// }, 0, 2))
// fmt.Println(validPath(6, [][]int{
// {0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3},
// }, 0, 5))
// fmt.Println(validPath(10, [][]int{
// {0,7},{0,8},{6,1},{2,0},{0,4},{5,8},{4,7},{1,3},{3,5},{6,5},
// }, 7, 5))
// }


