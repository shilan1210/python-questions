n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)
sorted_flag = True
for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        sorted_flag = False
        break
if sorted_flag:
    print("sorted")
else:
    print("not sorted")