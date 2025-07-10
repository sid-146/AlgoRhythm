package main
import "fmt"

func insertion_sort(arr []int, n int){
	for i := 0; i < n; i++{
		j := i
		for j>0 && arr[j-1] > arr[j] {
			var temp int = arr[j-1]
			arr[j-1] = arr[j]
			arr[j] = temp
			j--
		}

	}
}

func main() {
	arr := []int8{22, 11, 33, 44, 66, 55} // Inferred length
	var n int = len(arr)
	insertion_sort(arr, n)
	fmt.Println(arr)
}
