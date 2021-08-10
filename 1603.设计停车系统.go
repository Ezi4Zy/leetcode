/*
 * @lc app=leetcode.cn id=1603 lang=golang
 *
 * [1603] 设计停车系统
 */

// @lc code=start
package main

type ParkingSystem struct {
	freePark *[3]int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{
		freePark: &[3]int{big, medium, small},
	}

}

func (this *ParkingSystem) AddCar(carType int) bool {
	this.freePark[carType-1]--
	return this.freePark[carType-1] >= 0

}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */
// @lc code=end
