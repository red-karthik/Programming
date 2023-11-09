def quick_sort(arr):

    if(len(arr) <= 1):
        return arr
    print("len",len(arr))
    pivot = arr[len(arr) // 2]
    print("pivot = ", pivot)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


user_numbers = input()
arr = [int(num) for num in user_numbers.split(',')]
sorted_list = quick_sort(arr)
print(sorted_list)