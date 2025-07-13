#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void merge(int arr[], int low, int mid, int high)
{
    vector<int> v;
    int left = low;
    int right = mid + 1;
    while (left <= mid && right <= high)
    {
        if (arr[left] <= arr[right])
        {

            v.push_back(arr[left]);
            left++;
        }
        else
        {
            v.push_back(arr[right]);
            right++;
        }
    }

    while (left <= mid)
    {
        v.push_back(arr[left]);
        left++;
    }

    while (right <= high)
    {
        v.push_back(arr[right]);
        right++;
    }

    for (int i = low; i <= high; i++)
    {
        arr[i] = v[i - low];
    }
}

void mergeSort(int arr[], int low, int high)
{
    if (low >= high)
        return;

    int mid = (low + high) / 2;
    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);
    merge(arr, low, mid, high);
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90, 78};
    int high = sizeof(arr) / sizeof(arr[0]);
    int low = 0;

    mergeSort(arr, low, high - 1);
    cout << "Sorted array: \n";
    for (int i = 0; i < high; i++)
        cout << arr[i] << " ";
    cout << endl;
    return 0;
}
