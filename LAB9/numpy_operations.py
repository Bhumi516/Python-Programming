
# # Install numpy and check the version

# import numpy as np

# print("NumPy version:", np.__version__)


# # 1D, 2D, 3D array creation and printing operation

# # 1D
# import numpy as np
# arr1=np.array([10,20,30,40,50])
# print("1D Array: ", arr1)


# # 2D
# import numpy as np
# arr2=np.array([[10,20,30,40],[50,60,70,80]])
# print("2D Array: ", arr2)



# # 3D
# import numpy as np

# arr3 = np.array([
#     [
#         [1, 2],
#         [3, 4]
#     ],
#     [
#         [5, 6],
#         [7, 8]
#     ]
# ])

# print("3D Array:")
# print(arr3)



# Addition, Subtraction, Multiplication and Division on 2D Array


# import numpy as np

# A = np.array([
#     [10, 20],
#     [30, 40]
# ])

# B = np.array([
#     [1, 2],
#     [3, 4]
# ])

# print("Array A:")
# print(A)

# print("\nArray B:")
# print(B)

# print("\nAddition:")
# print(A + B)

# print("\nSubtraction:")
# print(A - B)

# print("\nMultiplication:")
# print(A * B)

# print("\nDivision:")
# print(A / B)



# Transpose of 2D Array

# import numpy as np

# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print("Original Array:")
# print(A)

# print("\nTranspose:")
# print(A.T)




# Exponential Operation on 2D Array

# import numpy as np

# A = np.array([
#     [1, 2],
#     [3, 4]
# ])

# print("Original Array:")
# print(A)

# print("\nExponential:")
# print(np.exp(A))



# Add Character Label to Array

# import numpy as np

# data = np.array([
#     (1, 'A'),
#     (2, 'B'),
#     (3, 'C')
# ], dtype=[('Number', 'i4'), ('Label', 'U1')])

# print(data)



