import sys


def lcs(a, b, k, j):
    # base case
    if k == 0 or j == 0:
        return 0

    # if equal, then we store the value of the function call
    if a[k - 1] == b[j - 1]:
        return 1 + lcs(X, Y, k - 1, j - 1)

    else:
        return max(lcs(X, Y, k, j - 1), lcs(X, Y, k - 1, j))


# Driver Code

sys.setrecursionlimit(10000)
X = input()
Y = input()
n = len(X)

print(lcs(X, Y, n, n))
