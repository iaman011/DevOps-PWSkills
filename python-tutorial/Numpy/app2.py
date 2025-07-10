import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])

print(np.add(x,y))
print("-"*15)
print(np.multiply(x,y))
print("-"*15)
print(np.dot(x,y))
print("-"*15)
print(np.exp(x))
print("-"*15)
print(np.sqrt(y))
print("-"*15)

arr=np.array(
    [
        [1,2],
        [3,4]
    ]
)

print(np.mean(arr))  #average
print("-"*15)
print(np.std(arr))  #Standard Deviation
print("-"*15)
print(np.min(arr)) #minimum
print("-"*15)
print(np.max(arr)) # maximum
print("-"*15)
print(np.sum(arr, axis=0)) #sum by columns: [4,6]
print("-"*15)
print(np.sum(arr, axis=1)) #Sum by rows: [3,7]
print("-"*15)
