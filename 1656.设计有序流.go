/*
 * @lc app=leetcode.cn id=1656 lang=golang
 *
 * [1656] 设计有序流
 */

// @lc code=start
package main

type OrderedStream struct {
	index int
	data  []string
	len   int
}

func Constructor(n int) OrderedStream {
	return OrderedStream{
		index: 0,
		len:   n,
		data:  make([]string, n),
	}

}

func (this *OrderedStream) Insert(idKey int, value string) []string {
	this.data[idKey-1] = value
	start := this.index
	for this.index < this.len && this.data[this.index] != "" {
		this.index++
	}
	return this.data[start:this.index]
}

//
// func main() {
// os := Constructor(5)
// fmt.Println(os.Insert(3, "cccc"), os.index)
// fmt.Println(os.Insert(1, "aaaa"), os.index)
// fmt.Println(os.Insert(2, "bbbb"), os.index)
// fmt.Println(os.Insert(5, "eeee"), os.index)
// fmt.Println(os.Insert(4, "dddd"), os.index)
// }

/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(idKey,value);
 */
// @lc code=end
