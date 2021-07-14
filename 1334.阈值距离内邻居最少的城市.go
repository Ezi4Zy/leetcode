/*
 * @lc app=leetcode.cn id=1334 lang=golang
 *
 * [1334] 阈值距离内邻居最少的城市
 */

// @lc code=start
// package leetcode

func findTheCity(n int, edges [][]int, distanceThreshold int) int {
	var dp [][]int
	for i := 0; i < n; i++ {
		var tmp []int
		for j := 0; j < n; j++ {
			if i == j {
				tmp = append(tmp, 0)
			} else {
				tmp = append(tmp, -1)
			}
		}
		dp = append(dp, tmp)
	}
	for i := 0; i < len(edges); i++ {
		dp[edges[i][0]][edges[i][1]] = edges[i][2]
		dp[edges[i][1]][edges[i][0]] = edges[i][2]
	}

	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if i == j || j == k || i == k {
					continue
				}
				if dp[i][k] == -1 || dp[k][j] == -1 {
					continue
				}
				if dp[i][j] == -1 || dp[i][j] > dp[i][k]+dp[k][j] {
					dp[i][j] = dp[i][k] + dp[k][j]
					dp[j][i] = dp[i][k] + dp[k][j]
				}
			}
		}
	}
	m := n
	ret := 0
	for i := 0; i < n; i++ {
		count := 0
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			if dp[i][j] <= distanceThreshold {
				count += 1
			}
		}
		if count <= m {
			ret = i
			m = count
		}
	}
	return ret
}

// @lc code=end
