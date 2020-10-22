"""
Largest subarray with sum 0
"""
def maxLen(n, arr):
    sumArr = [0]*n
    sumArr[0] = arr[0]
    countMap = {}
    countMap[arr[0]] = 0
    for i in range(1, n):
        sumArr[i] = arr[i] + sumArr[i-1]
        if sumArr[i] not in countMap:
            countMap[sumArr[i]] = 1
        else:
            countMap[sumArr[i]] += 1
    # print("Sum Arr : ",*sumArr)
    # print("Count Map : ",countMap)
    freqValue = max(countMap.items(), key= lambda i:i[1])[0]
    firstOccr = sumArr.index(freqValue)
    lastOccr = len(sumArr) - sumArr[::-1].index(freqValue) - 1
    return lastOccr - firstOccr+





if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        result = maxLen(n, arr)
        print(result)