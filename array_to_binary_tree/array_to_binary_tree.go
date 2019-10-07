/***
Construct a complete binary tree from given array in level order fashion
https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
*/
package main

import "fmt"

type node struct {
	left *node
	right *node
	data int
}

func (bt *node)insertLevelOrder(arr []int, i, arrlen int) *node {
	if  i < arrlen {
		temp := &node{left: nil, right: nil, data: arr[i]}
		bt = temp

		// insert left child
		bt.left = bt.left.insertLevelOrder(arr, 2 * i + 1, arrlen)

		// insert right child
		bt.right = bt.right.insertLevelOrder(arr, 2 * i + 2, arrlen)
	}
	return bt
}

func (bt *node)inorder() {
	if bt != nil {
		bt.left.inorder()
		fmt.Printf("%d ",bt.data)
		bt.right.inorder()
	}
}

func main() {
	bt := new(node)
	arr := []int{1, 2, 3, 4, 5, 6, 6, 6, 6 }
	lenArr := len(arr)
	root := bt.insertLevelOrder(arr, 0, lenArr)
	root.inorder()
}