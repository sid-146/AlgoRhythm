from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        freq = Counter()
        topx = SortedList()   # sorted ascending by (freq, val)
        rest = SortedList()   # same key
        total = 0
        res = []

        def remove_item(item):
            nonlocal total
            if item in topx:
                topx.remove(item)
                total -= item[0] * item[1]
            elif item in rest:
                rest.remove(item)

        def add_item_to_rest(item):
            rest.add(item)

        def rebalance():
            nonlocal total
            while len(topx) < x and rest:
                item = rest.pop()   # largest by (freq, val)
                topx.add(item)
                total += item[0] * item[1]

            while len(topx) > x:
                item = topx.pop(0)  # smallest in topx
                rest.add(item)
                total -= item[0] * item[1]

            while rest and topx and rest[-1] > topx[0]:
                r_item = rest.pop()     # candidate to move up (largest in rest)
                t_item = topx.pop(0)    # smallest in topx to move down
                # swap
                topx.add(r_item)
                rest.add(t_item)
                # adjust total: remove t_item contribution, add r_item contribution
                total -= t_item[0] * t_item[1]
                total += r_item[0] * r_item[1]

        def update(num, delta):
            # update frequency of num by delta (+1 or -1)
            oldf = freq.get(num, 0)
            if oldf > 0:
                remove_item((oldf, num))
            newf = oldf + delta
            if newf > 0:
                freq[num] = newf
                add_item_to_rest((newf, num))
            else:
                # frequency went to zero -> remove from map if present
                if num in freq:
                    del freq[num]
            rebalance()

        # initialize first window
        for i in range(k):
            update(nums[i], 1)
        res.append(total)

        # slide window
        for i in range(k, n):
            update(nums[i - k], -1)  # remove outgoing
            update(nums[i], 1)       # add incoming
            res.append(total)

        return res
