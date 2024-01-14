package main

import (
	"fmt"
	"math/rand"
)

func QuickSort(list []int) []int {
	// base case
	if len(list) <= 1 {
		return list
	}

	pivot := list[len(list)/2]

	// Partition the list into three parts: less than, equal to, and greater than the pivot
	var left, middle, right []int

	for _, num := range list {
		if num < pivot {
			left = append(left, num)
		} else if num == pivot {
			middle = append(middle, num)
		} else {
			right = append(right, num)
		}
	}

	return append(append(QuickSort(left), middle...), QuickSort(right)...)
}

func main() {
	num := 50

	unsortedList := make([]int, num)
	for i := 0; i < num; i++ {
		unsortedList[i] = rand.Intn(num) + 1
	}
	fmt.Println("Unsorted list:", unsortedList)

	sortedList := QuickSort(unsortedList)
	fmt.Println("Sorted list:", sortedList)
}
