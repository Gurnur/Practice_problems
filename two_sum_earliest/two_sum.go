/****
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 */
package main

import "fmt"

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)
	for i := range nums {
		if item, exists := seen[target - nums[i]]; exists {
			return []int{item, i}
		}
		seen[nums[i]] = i
	}
	return nil
}

func main(){
	result := twoSum([]int{9,2,1,11,15,7,8}, 9)
	fmt.Println(result)
}