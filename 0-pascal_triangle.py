def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle of n.

    Args:
    n (int): The number of rows in Pascal's Triangle.

    Returns:
    list: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start the row with 1
        row = [1]

        # Calculate the values in between the first and last element
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End the row with 1, if it's not the first row
        if i > 0:
            row.append(1)

        # Add the row to the triangle
        triangle.append(row)

    return triangle
