# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    
    indexOfA = 0
    indexOfB = 0

    while indexOfA < len(arrA) and indexOfB < len(arrB):
        if arrA[indexOfA] < arrB[indexOfB]:
            merged_arr.append(arrA[indexOfA])
            indexOfA += 1
        else: 
            merged_arr.append(arrB[indexOfB])
            indexOfB += 1

    merged_arr += arrA[indexOfA:]      
    merged_arr += arrB[indexOfB:]    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    length = len(arr)
    if length <= 1:
        return arr

    mid = length // 2
    half1 = arr[:mid]
    half2 = arr[mid:]
    arrA = merge_sort(half1)
    arrB = merge_sort(half2)
    return merge(arrA, arrB)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
