def linear(arr, num):
    count = 1
    for i in arr:
        count += 1 
        if i == num:
            return(f"Position {count}") 

def binary(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return mid
        
        if arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binary(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")
