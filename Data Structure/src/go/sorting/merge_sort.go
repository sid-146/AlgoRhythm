package main

import "fmt"

func merge(arr []int, low int, mid int, high int) {
	var left int = low
	var right int = mid + 1
	var temp []int

	for left <= mid && right <= high {
		if arr[left] <= arr[right] {
			temp = append(temp, arr[left])
			left++
		} else {
			temp = append(temp, arr[right])
			right++
		}
	}

	for left <= mid {
		temp = append(temp, arr[left])
		left++
	}

	for right <= high {
		temp = append(temp, arr[right])
		right++
	}

	for i := low; i <= high; i++ {
		arr[i] = temp[i-low]
	}

}

func merge_sort(arr []int, low int, high int) {
	if low >= high {
		return
	}
	var mid int = (low + high) / 2
	merge_sort(arr, low, mid)
	merge_sort(arr, mid+1, high)
	merge(arr, low, mid, high)
}

func main() {
	arr := []int{64, 34, 25, 12, 22, 11, 90, 78}
	var high int = len(arr)
	var low int = 0
	merge_sort(arr, low, high-1)
	fmt.Println("Sorted Array: ", arr)
}
