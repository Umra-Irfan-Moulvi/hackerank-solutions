def diagonalDifference(arr):
    n = len(arr)

    primary = 0
    secondary = 0

    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n - 1 - i]

    return abs(primary - secondary)


# Get input
n = int(input("Enter the size of the matrix: "))

arr = []

print("Enter the matrix:")

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# Calculate and display result
result = diagonalDifference(arr)

print("Diagonal Difference:", result)