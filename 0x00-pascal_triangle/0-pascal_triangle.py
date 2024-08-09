def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]  # Every row starts with 1

        # Generate the middle values of the current row
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)  # Every row ends with 1
        triangle.append(current_row)

    return triangle

# Example usage:
n = 5
triangle = pascal_triangle(n)
for row in triangle:
    print(row)

