from utils.utils import Utils

# To find Majority element in array

"""
    majority element if count(majority element) > N/2 where N is length of list
"""


def verify(ME: int, arr: list):
    if ME == -1:
        return False
    votes = 0
    for i in arr:
        if i == ME:
            votes = votes + 1

    majority = int(len(arr) / 2)
    # print(len(arr))
    # print(ME,votes)
    # print()
    # print(majority)
    if votes > majority:
        return True
    else:
        return False


def getCandidate(arr: list):
    votes = 0
    ME = -1
    for i in arr:
        if votes == 0:
            ME = i
            votes = 1

        if i == ME:
            votes = votes + 1
        else:
            votes = votes - 1
    return ME


if __name__ == "__main__":
    arr = Utils().getRandomArray(5, 1, 5)
    print(arr)
    # arr = utils.getRandomArray()
    me = getCandidate(arr)
    result = verify(me, arr)
    if result:
        print(f"{me} is in majority")
    else:
        print(f"No majority element")
