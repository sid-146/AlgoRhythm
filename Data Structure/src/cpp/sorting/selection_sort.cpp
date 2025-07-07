#include <iostream>

using namespace std;

void selectionSort(int arr[], int n)
{
    int min_index, swap_counter = 0;
    for (int i = 0; i < n - 1; i++)
    {
        min_index = i;
        for (int j = i; j < n; j++)
        {
            if (arr[j] < arr[min_index])
            {
                min_index = j;
            }
        }
        if (min_index != i)
        {
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
            swap_counter++;
        }
    }
    cout << "Number of Swaps: " << swap_counter << endl;
}

int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSort(arr, n);
    cout << "Sorted array: \n";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    return 0;
}