import numpy as np

# Define the array
array = np.array([[1,  2,  3], 
                  [4,  5,  6], 
                  [7,  8,  9]])

# Calculate the sum of rows and columns
row_sums = array.sum(axis=1)
col_sums = array.sum(axis=0)

# Print the array with sums beside and under the columns without the total sum at the bottom right
result_str = ""

for i in range(array.shape[0]):
    result_str += " ".join(map(str, array[i])) + " | " + str(row_sums[i]) + "\n"

result_str += "- " * array.shape[1] + "\n"

result_str += " ".join(map(str, col_sums)) + "\n"

print(result_str)
