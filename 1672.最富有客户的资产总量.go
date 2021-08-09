/*
 * @lc app=leetcode.cn id=1672 lang=golang
 *
 * [1672] 最富有客户的资产总量
 */

// @lc code=start
package main

func maximumWealth(accounts [][]int) int {
	maximumAsset := 0
	for i := 0; i < len(accounts); i++ {
		asset := 0
		for j := 0; j < len(accounts[i]); j++ {
			asset += accounts[i][j]
		}
		if asset > maximumAsset {
			maximumAsset = asset
		}
	}
	return maximumAsset
}

// @lc code=end
