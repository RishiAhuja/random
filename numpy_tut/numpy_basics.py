import numpy as np

#initializing an array

a = np.array([1,2,3]) #pass a list
print(a)

#multi dimentional arrays

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(b)

#get dimension of an array
print(a.ndim)
print(b.ndim)

#get shape of the matrix
print(a.shape) #(3,)
print(b.shape) #(2, 3)

#get type
print(a.dtype) #by default it is int64

#we can specify how much space each integer requires
c = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ], dtype='int8'
)

print(c.dtype)

#get size
print(a.itemsize)
print(c.itemsize)

#total size
print(a.itemsize * a.size) #size of each element * total number of elements
print(a.nbytes)


#accessing elements of a specific column and row

d = np.array(
    [
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 0, 1, 2, 3, 4]
    ]
)

print(d)
print(d.shape)
print(d[1, 5]) #d[r, c]
print(d[1, -2]) #d[r, c]

#get a specific row or column with slicing
print(d[0, :])
print(d[:, 4])

#replacing numbers
d[0, 3] = 5
print(d)

#3 dimentional arrays
array_3d = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])

print(array_3d[0, 1, 2]) #layer, row, column

random_array_decimal = np.random.rand(4, 2)
random_array_int = np.random.randint(7, size=(3,4)) #will generate from (0, 6)

print(random_array_decimal)
print(random_array_int)

#indentity matrix
l = np.identity(5) # 5x5 identity matrix
print(l)

#repeating
k = np.array([
    [1, 2, 3]
])

k1 = np.repeat(k, 3, axis=1)
'''
for axis = 0
[[1 2 3]
 [1 2 3]
 [1 2 3]]

for axis = 1
[[1 1 1 2 2 2 3 3 3]]
'''

print(k1)


#shallow copy vs deep copy

#shallow

a1 = np.zeros(5)
b1 = a1

#deep 

b1 = a1.copy() 

##maths
np.cos(b1)

print(b1)

a1 + 2
print(a1)

##linear algebbra

a2 = np.ones((2, 3))    # Shape (2, 3)
b2 = np.full((3, 2), 2) # Shape (3, 2)

print(a2)
print(b2)

c = np.matmul(a2,b2)
print(c)

print(np.linalg.det(c))
