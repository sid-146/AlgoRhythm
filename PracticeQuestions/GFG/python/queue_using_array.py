"""
Implement a Queue using an Array. Queries in the Queue are of the following type:
1. 1 x   (a query of this type means  pushing 'x' into the queue)
2. 2     (a query of this type means to pop an element from the queue and print the popped element. If the queue is empty then return -1)

We just have to implement the functions push and pop and the driver code will handle the output.

Examples:

Input: Queries = `1 2 1 3 2 1 4 2`
Output: `2 3`
Explanation: For query 1 2 the queue will be {2} 1 3 the queue will be {2 3} 2   poped element will be 2 the queue will be {3} 1 4 the queue will be {3 4} 2 poped element will be 3

Input: Queries = `1 3 2 2 1 4`
Output: `3 -1`
Explanation: For query 1 3 the queue will be {3} 2 poped element will be 3 the queue will be empty 2 there is no element in the queue and hence -1 1 4 the queue will be {4}.

Input: Queries = `1 3 2 2 1 3`
Output: `3 -1`
Explanation: For query 1 3 the queue will be {3} 2 poped element will be 3 the queue will be empty 2 there is no element in the queue and hence -1 1 3 the queue will be {3} and hence -1 1 3 the queue will be {3}.

Constraints:
1 ≤ `number of query` ≤ 105
0 ≤ `x` ≤ 105
"""

# User function Template for python3

# LIFO

# []
# Push 1
# [1]
# Push 2
# [1 2]
# Push 3
# [1 2 3]
# pop [1 2 3]
# 1 [2 3]


class MyQueue:
    # Function to push an element x in a queue.
    def __inti__(self):
        self.queue: list = []

    def push(self, x):
        # add code here
        self.queue.append(x)

    # Function to pop an element from queue and return that element.
    def pop(self):
        return self.queue.pop(0)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = MyQueue()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while i < len(q1):
            if q1[i] == 1:
                s.push(q1[i + 1])
                i = i + 2
            elif q1[i] == 2:
                print(s.pop(), end=" ")
                i = i + 1
            elif s.isEmpty():
                print(-1)
                i = i + 1
        print()

        print("~")
# } Driver Code Ends
