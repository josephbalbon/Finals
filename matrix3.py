matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='\t')
    if i == 0:
        print('\t\t', diagonal_sum)  
    elif i == 1:
        print('\t', diagonal_sum)    
    else:
        print()
