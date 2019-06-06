# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  
  return -1

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  mid = (low + high) // 2

  
  while True:
    if arr[mid] == target:
      return mid
    elif target < arr[mid]:
      # eliminate RHS
      high = mid
      mid = (low + high) // 2
    elif target > arr[mid]:
      # eliminate LHS
      low = middle
      mid = (low + high) // 2
    else:
      return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  if arr[middle] == target:
    return middle
  elif target < arr[middle]:
    # eliminate RHS
    high = middle
    return binary_search_recursive(arr, target, low, high)
  elif target > arr[middle]:
    # eliminate LHS
    low = middle
    return binary_search_recursive(arr, target, low, high)
  else:
    return -1 # not found
