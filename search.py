import random
comparecount = 0
def binary_search(arr, low, high, x):
  global comparecount
  if high >= low:
    mid = (high + low) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      comparecount +=1
      print("comparecount = ",comparecount, "low = ",low, "high =",mid-1)
      return binary_search(arr, low, mid - 1, x)
    else:
      comparecount +=1
      print("comparecount = ",comparecount, "low = ",mid+1, "high =",high)
      return binary_search(arr, mid + 1 , high, x)
  else:
    return -1

def sequential_search(arr,x):
  global comparecount
  for i in arr:
    comparecount +=1
    if i==x:
      return comparecount
  return -1

datcount = 100000
## incase of sequential search
#arr = [random.randint(1,10000000) for i in range(datcount)]

## in case of binary search
arr = sorted([random.randint(1,10000000) for i in range(datcount)])

## in case of succesfully search
#x = arr[random.randint(1,datcount)]

## in case of unsuccessfully search
#x = -1

## worstcase successfully search
x = arr[-1]

print("key =",x)
print("data len = ",len(arr))

## in case of binary search
result = binary_search(arr, 0, len(arr)-1, x)
## incase of sequential search
#result = sequential_search(arr,x)

print("compare count = " ,comparecount)
if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
