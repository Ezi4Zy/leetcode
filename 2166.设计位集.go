/*
 * @lc app=leetcode.cn id=2166 lang=golang
 *
 * [2166] 设计位集
 */
package main

import "bytes"

// @lc code=start
type Bitset struct {
	bits   []byte
	cnt    int
	isFlip bool
}

func Constructor(size int) Bitset {
	bitset := Bitset{
		bits:   bytes.Repeat([]byte{'0'}, size),
		cnt:    0,
		isFlip: false,
	}
	return bitset
}

func (this *Bitset) value(idx int) byte {
	if (this.bits[idx] == '0' && !this.isFlip) || (this.bits[idx] == '1' && this.isFlip) {
		return '0'
	} else {
		return '1'
	}
}

func (this *Bitset) Fix(idx int) {
	if this.value(idx) == '0' {
		this.cnt++
		if this.isFlip {
			this.bits[idx] = '0'
		} else {
			this.bits[idx] = '1'
		}
	}
}

func (this *Bitset) Unfix(idx int) {
	if this.value(idx) == '1' {
		this.cnt--
		if this.isFlip {
			this.bits[idx] = '1'
		} else {
			this.bits[idx] = '0'
		}
	}
}

func (this *Bitset) Flip() {
	this.isFlip = !this.isFlip
	this.cnt = len(this.bits) - this.cnt

}

func (this *Bitset) All() bool {
	return this.cnt == len(this.bits)
}

func (this *Bitset) One() bool {
	return this.cnt > 0
}

func (this *Bitset) Count() int {
	return this.cnt
}

func (this *Bitset) ToString() string {
	if this.isFlip {
		for i := 0; i < len(this.bits); i++ {
			this.bits[i] = this.value(i)
		}
		this.isFlip = false
	}
	return string(this.bits)
}

/**
 * Your Bitset object will be instantiated and called as such:
 * obj := Constructor(size);
 * obj.Fix(idx);
 * obj.Unfix(idx);
 * obj.Flip();
 * param_4 := obj.All();
 * param_5 := obj.One();
 * param_6 := obj.Count();
 * param_7 := obj.ToString();
 */
// @lc code=end
