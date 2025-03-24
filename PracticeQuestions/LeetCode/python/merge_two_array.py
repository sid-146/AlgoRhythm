from typing import List


def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    nums_dict = {}

    def merge(arr: list[int], nums_dict: dict):
        for i in range(len(arr)):
            key, value = arr[i]
            exist = nums_dict.get(key, 0)
            nums_dict[key] = exist + value

        return nums_dict

    nums_dict = merge(nums1, nums_dict)
    nums_dict = merge(nums2, nums_dict)

    result = [[k, v] for k, v in nums_dict.items()]
    result.sort(key=lambda x: x[0])

    return result


if __name__ == "__main__":

    result = mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]])
    print(result)
