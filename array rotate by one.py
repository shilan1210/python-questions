n = int(input("Enter number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)
last = arr[-1]
# Shift elements to the right
for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]
arr[0] = last
print("Array after rotating by one:")
for num in arr:
    print(num, end=' ')
