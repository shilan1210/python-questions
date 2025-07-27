n = int(input("Enter number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)
# Reverse logic using swap
for i in range(n // 2):
    temp = arr[i]
    arr[i] = arr[n - i - 1]
    arr[n - i - 1] = temp
print("Reversed array:")
for i in arr:
    print(i, end=' ')