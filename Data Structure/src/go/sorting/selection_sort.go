package main

import "fmt"

func selection_sort(arr []int, n int) {
	var swap_counter int = 0
	for i := 0; i < n; i++ {
		min_index := i
		for j := i; j < n; j++ {
			if arr[j] < arr[min_index] {
				min_index = j
				swap_counter++
			}
		}
		if min_index != i {
			arr[i], arr[min_index] = arr[min_index], arr[i]
		}
	}
	fmt.Println("Number of Swaps: ", swap_counter)
}

func main() {
	arr := []int{22, 11, 33, 44, 66, 55} // Inferred length
	var n int = len(arr)
	selection_sort(arr, n)
	fmt.Println(arr)
}
