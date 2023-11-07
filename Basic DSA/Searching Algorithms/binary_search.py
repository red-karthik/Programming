def binary_search(arr, search_num):
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = (first + last)// 2
        if arr[mid] == search_num:
            return mid
        elif arr[mid] < search_num:
            first = mid + 1
        elif arr[mid] > search_num:
            last = mid - 1
    return -1
print(binary_search([0,1,2,3,4,5,6],5))