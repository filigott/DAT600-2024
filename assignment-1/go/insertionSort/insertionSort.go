package main

import (
	"fmt"
	"math/rand"
)

// InsertionSort sorts a slice of integers using the insertion sort algorithm
func InsertionSort(slice []int) []int {
	n := len(slice)

	// Create a copy of the slice to avoid modifying the original slice
	list := make([]int, n)
	copy(list, slice)

	for i := 1; i < n; i++ {
		key := list[i]
		j := i - 1

		for j >= 0 && key < list[j] {
			list[j+1] = list[j]
			j--
		}

		list[j+1] = key
	}
	return list
}

func main() {
	num := 50

	unsortedList := make([]int, num)
	for i := 0; i < num; i++ {
		unsortedList[i] = rand.Intn(num) + 1
	}
	fmt.Println("Unsorted list:", unsortedList)

	sortedList := InsertionSort(unsortedList)
	fmt.Println("Sorted list:", sortedList)
}
