# Define tuples
x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)

# Print original tuples
print("Original tuples:")
print(x)
print(y)
print(z)

# Element-wise sum of the tuples
print("\nElement-wise sum of the said tuples:")
result = tuple(map(sum, zip(x, y, z)))
print(result)

# Import numpy and define lists
from numpy import array

lst1 = [1, 5, 7]
lst2 = [3, 2, 1]

# Convert lists to numpy arrays and print the sum
a = array(lst1)
b = array(lst2)
print("\nSum of numpy arrays:")
print(a + b)
