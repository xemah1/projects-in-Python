import random

arr = []
for i in range(10) :
    arr.append((random.randint(0,99) + 1))
cool = arr[random.randint(0,len(arr) - 1)]
arr.sort()

def binarySearch (arr, cool) :
    high = len(arr) - 1
    low = 0

    while high > low :
        middle = (high + low) // 2
        if (arr[middle] > cool) :
            high = middle - 1
        elif (arr[middle] < cool) :
            low = middle + 1
        else :
            return middle
    return -1

result = binarySearch(arr,cool)
print("Number Searched: " + str(cool))
if (result != -1) :
    print("Index: " + str(result))
else :
    print("Number is not present.")
print(arr)