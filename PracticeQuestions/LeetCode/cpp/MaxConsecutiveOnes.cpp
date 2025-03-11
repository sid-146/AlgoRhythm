#include <iostream>

using namespace std;

int maxConsecutive(int *arr, int size)
{
    int high = 0;
    int counter = 0;

    // cout<<size<<endl;
    if (size < 1)
    {
        // cout<<"inside size check"<<endl;
        return 0;
    }

    for (int i = 0;i <= size ; i++)
    {
        // cout << arr[i] << endl;
        if (arr[i] == 0)
        {
            counter = 0;
        }
        else if (arr[i] == 1)
        {
            counter++;
            if (counter > high)
            {
                high = counter;
            }
        }
        else
        {
            return 0;
        }
    }

    return high;
}

int main()
{
    int arr[] = {1, 1, 0, 1, 1, 1};
    cout << maxConsecutive(arr, 6) << endl;
    return 0;
}