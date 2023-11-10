def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

user_numbers = input()
arr = [int(num) for num in user_numbers.split(',')]
sorted_list = bubble_sort(arr)
print(sorted_list)