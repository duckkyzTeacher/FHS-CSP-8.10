# Problem 1: Create a 2D list
# Task: Create a 2D list called `matrix` representing the following table:
# 1  2  3
# 4  5  6
# 7  8  9
# Print the entire matrix, then print the first row and the last column.




# Problem 2: Modify the 2D list
# Task: Starting with the `matrix` from Problem 1, update the value `5` to `10`
# and add a new row [10, 11, 12]. Print the modified matrix.




# Problem 3: Seat assignment
# Task: Create a 2D list that represents the seating arrangement of a classroom with 3 rows and 4 seats per row.
# Assign students to 5 seats by placing their names in the list. Print the seating arrangement before and after.




# Problem 4: Nested loops
# Task: Write a program that prints all the elements in the `matrix` (from Problem 1) in a formatted grid using nested `for` loops.




# Problem 5: Fix the code
# The following code has a logic error and prints the wrong values from the matrix.
# Fix the logic so it prints each element in row 2 (the second row).
# Expected Output: 4 5 6

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix[1])):
    print(matrix[i][1])





# Problem 6: Logic fix
# The following code is supposed to change all the elements in the first row of the matrix to 0,
# but it doesn't work as intended. Fix the error.
# Expected Output: [[0, 0, 0], [4, 5, 6], [7, 8, 9]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for element in matrix:
    element[0] = 0
print(matrix)




