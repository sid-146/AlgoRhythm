package main

import "fmt"

func bubble_sort(arr []int, n int) {
	swap_counter := 0
	swapped := false
	for i := n - 1; i > 1; i-- {
		for j := 0; j < i; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap_counter++
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
	fmt.Println("Number of swaps : ", swap_counter)

}

func main() {
	arr := []int{64, 34, 25, 12, 22, 11, 90}
	n := len(arr)
	fmt.Println("Unsorted array:", arr)
	bubble_sort(arr, n)
	fmt.Println("Sorted array:", arr)

	arr2 := []int{1, 2, 3, 3, 4, 5, 6}
	n2 := len(arr)
	fmt.Println("Unsorted array:", arr)
	bubble_sort(arr2, n2)
	fmt.Println("Sorted array:", arr)
}
