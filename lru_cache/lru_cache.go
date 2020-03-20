/**
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1. put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before
inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

**/

package main

import "fmt"

type node struct {
	prev *node
	next *node
	key  int
	val  int
}

// doubly linked list
type dll struct {
	head *node
	tail *node
}

// add the newly accessed value
func (root *dll) prepend(key, val int) {
	newNode := new(node)
	newNode.key = key
	newNode.val = val
	if root.head == nil {
		root.head = newNode
		root.tail = newNode
	} else {
		root.head.prev = newNode
		newNode.next = root.head
		root.head = newNode
	}
}

// remove the least recently used value
func (root *dll) removeTailNode() {
	if root.tail != nil {
		if root.tail.prev == nil {
			root.head = nil
			root.tail = nil
		} else {
			root.tail.prev.next = nil
			root.tail = root.tail.prev
		}
	}
}

// most recently used cache brought to the front
func (root *dll) moveToFront(n *node) {
	if n.prev != nil {
		if n.next == nil {
			n.prev.next = nil
			root.tail = n.prev
		} else {
			n.prev.next = n.next
			n.next.prev = n.prev
		}
		n.prev = nil
		n.next = root.head
		root.head.prev = n
		root.head = n
	}
}

func (root *dll) printList() {
	for n := root.head; n != nil; n = n.next {
		fmt.Printf("%v", n.val)
	}
}

// LRUCache datastructure
type LRUCache struct {
	maxlen   int
	curlen   int
	valueMap map[int]*node
	dNode    *dll
}

func Constructor(capacity int) LRUCache {
	cache := new(LRUCache)
	cache.maxlen = capacity
	cache.valueMap = make(map[int]*node)
	cache.dNode = new(dll)
	return *cache
}

func (this *LRUCache) Get(key int) int {
	if v, found := this.valueMap[key]; found {
		this.dNode.moveToFront(v)
		return v.val
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key, value int) {
	if this.maxlen == 0 {
		return
	}
	if v, found := this.valueMap[key]; found {
		this.dNode.moveToFront(v)
	} else {
		if this.curlen < this.maxlen {
			this.curlen += 1
		} else {
			delete(this.valueMap, this.dNode.tail.key)
			this.dNode.removeTailNode()
		}
		this.dNode.prepend(key, value)
		this.valueMap[key] = this.dNode.head
	}
}

func main() {
	obj := Constructor(3)
	obj.Put(1, 1)
	obj.Put(2, 2)
	obj.Put(3, 3)
	obj.Put(4, 4)
	fmt.Printf("%v\n", obj.Get(2))
	fmt.Printf("%v\n", obj.Get(3))
	obj.dNode.printList()
}
