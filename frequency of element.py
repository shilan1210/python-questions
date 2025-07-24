arr=[1,2,3,4,4,5,6,1,2]
freq={}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Frequency of elements:", freq)