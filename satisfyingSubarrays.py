#satisfyingsubarrays
# Since we actually care about all of the calculations,
# We will have to find all the calculations.
# Therefore, O(n^2) might be a good approach.

# Assumption: Only Positive Integers
def subarrays(arr, k):
    if arr == None or arr == []:
        return 0
    amountOfLists = 0
    for i in range(len(arr)):
        oddCount = 0
        for j in range(i, len(arr)):
            if arr[j] % 2 == 1:
                oddCount += 1
            if oddCount > k:
                break
            elif oddCount == k:
                amountOfLists += 1
    return amountOfLists

print(subarrays([1,4,6,8,10], 1))
