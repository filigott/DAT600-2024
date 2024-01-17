package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
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
func GenerateRandomList(n int) []int {
	list := make([]int, n)
	for i := 0; i < n; i++ {
		list[i] = rand.Intn(n)
	}
	return list
}

func main() {
	// Test execution time of quicksort
	max_list_length_digits := 6
	executionTimeSlice := make([]float64, max_list_length_digits-1)
	lengthsSlice := make([]int, max_list_length_digits-1)
	for i := 1; i < max_list_length_digits; i++ {
		n := math.Pow(float64(10), float64(i))
		fmt.Println(n)
		l := GenerateRandomList(int(n))
		timeStart := time.Now()
		_ = QuickSort(l)
		timeEnd := time.Now()
		executionTimeSlice[i-1] = timeEnd.Sub(timeStart).Seconds()
		lengthsSlice[i-1] = int(n)

	}
	fmt.Println(executionTimeSlice)
	fmt.Println(lengthsSlice)
}
