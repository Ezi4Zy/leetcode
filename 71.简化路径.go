/*
 * @lc app=leetcode.cn id=71 lang=golang
 *
 * [71] 简化路径
 */

// @lc code=start
package main

import (
	"strings"
)

type Node struct {
	name string
	next *Node
	pre  *Node
}

func simplifyPath1(path string) string {
	head := &Node{
		name: "",
	}
	head.pre = head
	start := 1
	end := 1
	cur := head
	for start < len(path) {
		for end < len(path) && path[end] != '/' {
			end++
		}
		name := path[start:end]
		if name == ".." {
			if name != "" {
				cur = cur.pre
				cur.next = nil
			}
		} else {
			if name != "." && name != "" {
				node := &Node{
					name: name,
					pre:  cur,
				}
				cur.next = node
				cur = node
			}
		}
		end++
		start = end
	}
	ret := "/"
	head = head.next
	for head != nil {
		ret += head.name
		if head.next != nil {
			ret += "/"
		}
		head = head.next
	}
	return ret
}

func simplifyPath(path string) string {
	realPaths := []string{}
	paths := strings.Split(path, "/")
	for i := 0; i < len(paths); i++ {
		path = paths[i]
		if path == "" || path == "." {
			continue
		}
		if path == ".." {
			if len(realPaths) > 0 {
				realPaths = realPaths[:len(realPaths)-1]
			}
			continue
		}
		realPaths = append(realPaths, path)
	}

	return "/" + strings.Join(realPaths, "/")
}

// func main() {
// fmt.Println(simplifyPath("/home/"))
// fmt.Println(simplifyPath("/../"))
// fmt.Println(simplifyPath("/home//foo/"))
// fmt.Println(simplifyPath("/a/./b/../../c/"))
// }

// @lc code=end
