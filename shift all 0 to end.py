n = int(input("Enter number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)
for i in range(0, n - 1):
    for j in range(i+1, n-1): 
        if(arr[i]==0 and arr[j]!=0):
            arr[i], arr[j] = arr[j], arr[i]
print("Array after shifting all zero to end:")
for num in arr:
    print(num, end=' ')
