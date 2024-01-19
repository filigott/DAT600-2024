package main

import (
	"fmt"
	"log"
	"math"
	"math/rand"
	"time"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
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

// GenerateRandomList generates a list of random integers of length n
func GenerateRandomList(n int) []int {
	list := make([]int, n)
	for i := 0; i < n; i++ {
		list[i] = rand.Intn(n)
	}
	return list
}

func main() {
	// Test execution time of InsertionSort
	max_list_length_digits := 7
	executionTimeSlice := make([]float64, max_list_length_digits-1)
	lengthsSlice := make([]int, max_list_length_digits-1)
	for i := 1; i < max_list_length_digits; i++ {
		n := math.Pow(float64(10), float64(i))
		fmt.Println(n)
		l := GenerateRandomList(int(n))
		timeStart := time.Now()
		_ = InsertionSort(l)
		timeEnd := time.Now()
		executionTimeSlice[i-1] = timeEnd.Sub(timeStart).Seconds()
		lengthsSlice[i-1] = int(n)

	}
	fmt.Println(executionTimeSlice)
	fmt.Println(lengthsSlice)

	// Create a new plot
	p := plot.New()

	// Create a scatter plot
	points := make(plotter.XYs, len(lengthsSlice))
	for i := range lengthsSlice {
		points[i].X = float64(lengthsSlice[i])
		points[i].Y = executionTimeSlice[i]
	}

	s, err := plotter.NewScatter(points)
	if err != nil {
		log.Fatal(err)
	}
	p.Add(s)

	line, err := plotter.NewLine(points)
	if err != nil {
		log.Fatal(err)
	}
	//line.Color = draw.ColorBlue
	p.Add(line)

	// Set axis labels
	p.X.Label.Text = "List Length"
	p.Y.Label.Text = "Execution Time"

	// Save the plot to a file
	if err := p.Save(6*vg.Inch, 6*vg.Inch, "scatter_plot_with_lines.png"); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Plot saved to scatter_plot_with_lines.png")
}
