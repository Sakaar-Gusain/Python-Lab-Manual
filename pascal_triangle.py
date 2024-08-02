#print out first n rows of Pascal's triangle
def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        # Each row starts with 1
        row = [1]

        # Build the rest of the row
        if i > 0:
            for j in range(1, i):
                # Each number (except the first and last of each row) is the sum of the two above it
                prev_row = triangle[i-1]
                row.append(prev_row[j-1] + prev_row[j])

            # Each row ends with 1
            row.append(1)

        # Add the current row to the triangle
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        # Print each number in the row, separated by spaces
        print(" ".join(map(str, row)))

# Get user input for number of rows
n = int(input("Enter the number of rows for Pascal's Triangle: "))

# Generate Pascal's Triangle
triangle = generate_pascals_triangle(n)

# Print Pascal's Triangle
print_pascals_triangle(triangle)
