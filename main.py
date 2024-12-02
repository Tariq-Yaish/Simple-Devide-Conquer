def maxSum(left, right):
    if left > right:
        return 0
    if left == right:
        return max(0, data[left])

    mid = (left + right) // 2

    sum = 0
    maxLeft = 0
    for i in range(mid, left, -1): #T(n/2)
        sum += data[i]
        maxLeft = max(maxLeft, sum)

    sum = 0
    maxRight = 0
    for i in range(mid + 1, right): #T(n/2)
        sum += data[i]
        maxRight = max(maxRight, sum)

    maxCross = maxLeft + maxRight
    maxA = maxSum(left, mid)
    maxB = maxSum(mid + 1, right)
    return max(maxCross, maxA, maxB)

data = [5, 3, -3, 0, 11, 0, -1, -3, 5, 6, 8, 9, 10]
lef = 0
rig = len(data) - 1
print(maxSum(lef, rig))
print(data)