/*
 * @lc app=leetcode.cn id=1882 lang=golang
 *
 * [1882] 使用服务器处理任务
 */
// package main

import (
	"container/heap"
)

type IdleServer struct {
	Index  int
	Weight int
}
type IdleServers []IdleServer

func (s IdleServers) Len() int      { return len(s) }
func (s IdleServers) Swap(i, j int) { s[i], s[j] = s[j], s[i] }
func (s IdleServers) Less(i, j int) bool {
	return s[i].Weight < s[j].Weight || s[i].Weight == s[j].Weight && s[i].Index < s[j].Index
}
func (s *IdleServers) Push(val interface{}) { *s = append(*s, val.(IdleServer)) }
func (s *IdleServers) Pop() interface{}     { ret := (*s)[len(*s)-1]; *s = (*s)[:len(*s)-1]; return ret }

type BusyServer struct {
	IdleServer
	FinishTime int
}

type BusyServers []BusyServer

func (s BusyServers) Len() int      { return len(s) }
func (s BusyServers) Swap(i, j int) { s[i], s[j] = s[j], s[i] }
func (s BusyServers) Less(i, j int) bool {
	return s[i].FinishTime < s[j].FinishTime || s[i].FinishTime == s[j].FinishTime && s[i].Weight < s[j].Weight || s[i].FinishTime == s[j].FinishTime && s[i].Weight == s[j].Weight && s[i].Index < s[j].Index
}
func (s *BusyServers) Push(val interface{}) { *s = append(*s, val.(BusyServer)) }
func (s *BusyServers) Pop() interface{}     { ret := (*s)[len(*s)-1]; *s = (*s)[:len(*s)-1]; return ret }

// @lc code=start
func assignTasks(servers []int, tasks []int) []int {
	ret := make([]int, len(tasks))
	idleServers := IdleServers(nil)
	for i := 0; i < len(servers); i++ {
		s := IdleServer{Weight: servers[i], Index: i}
		heap.Push(&idleServers, s)
	}
	busyServers := BusyServers(nil)
	for i, v := range tasks {
		for len(busyServers) > 0 && busyServers[0].FinishTime <= i {
			s := heap.Pop(&busyServers).(BusyServer)
			heap.Push(&idleServers, IdleServer{Weight: s.Weight, Index: s.Index})
		}
		if len(idleServers) != 0 {
			s := heap.Pop(&idleServers).(IdleServer)
			ret[i] = s.Index
			heap.Push(&busyServers, BusyServer{IdleServer: IdleServer{Index: s.Index, Weight: s.Weight}, FinishTime: i + v})
		} else {
			s := heap.Pop(&busyServers).(BusyServer)
			ret[i] = s.Index
			s.FinishTime += v
			heap.Push(&busyServers, s)
		}
	}
	return ret
}

// func main() {
// fmt.Println(assignTasks([]int{3, 3, 2}, []int{1, 2, 3, 2, 1, 2}))
// fmt.Println(assignTasks([]int{5, 1, 4, 3, 2}, []int{2, 1, 2, 4, 5, 2, 1}))
// fmt.Println(assignTasks([]int{10, 63, 95, 16, 85, 57, 83, 95, 6, 29, 71}, []int{70, 31, 83, 15, 32, 67, 98, 65, 56, 48, 38, 90, 5}))
// fmt.Println(assignTasks([]int{338, 890, 301, 532, 284, 930, 426, 616, 919, 267, 571, 140, 716, 859, 980, 469, 628, 490, 195, 664, 925, 652, 503, 301, 917, 563, 82, 947, 910, 451, 366, 190, 253, 516, 503, 721, 889, 964, 506, 914, 986, 718, 520, 328, 341, 765, 922, 139, 911, 578, 86, 435, 824, 321, 942, 215, 147, 985, 619, 865}, []int{773, 537, 46, 317, 233, 34, 712, 625, 336, 221, 145, 227, 194, 693, 981, 861, 317, 308, 400, 2, 391, 12, 626, 265, 710, 792, 620, 416, 267, 611, 875, 361, 494, 128, 133, 157, 638, 632, 2, 158, 428, 284, 847, 431, 94, 782, 888, 44, 117, 489, 222, 932, 494, 948, 405, 44, 185, 587, 738, 164, 356, 783, 276, 547, 605, 609, 930, 847, 39, 579, 768, 59, 976, 790, 612, 196, 865, 149, 975, 28, 653, 417, 539, 131, 220, 325, 252, 160, 761, 226, 629, 317, 185, 42, 713, 142, 130, 695, 944, 40, 700, 122, 992, 33, 30, 136, 773, 124, 203, 384, 910, 214, 536, 767, 859, 478, 96, 172, 398, 146, 713, 80, 235, 176, 876, 983, 363, 646, 166, 928, 232, 699, 504, 612, 918, 406, 42, 931, 647, 795, 139, 933, 746, 51, 63, 359, 303, 752, 799, 836, 50, 854, 161, 87, 346, 507, 468, 651, 32, 717, 279, 139, 851, 178, 934, 233, 876, 797, 701, 505, 878, 731, 468, 884, 87, 921, 782, 788, 803, 994, 67, 905, 309, 2, 85, 200, 368, 672, 995, 128, 734, 157, 157, 814, 327, 31, 556, 394, 47, 53, 755, 721, 159, 843}))
// }

// @lc code=end
