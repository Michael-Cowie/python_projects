'''Creates a 2DArray from input variables'''
x = int(input())
y = int(input())
column, row = x, y
matrix = [[0 for x in range(column)] for y in range(row)]
print(matrix)
