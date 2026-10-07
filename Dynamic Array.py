def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        query_type, x, y = query

        idx = (x ^ lastAnswer) % n

        if query_type == 1:
            arr[idx].append(y)

        elif query_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)

    return result


# Get input
first_multiple_input = input("Enter n and q: ").split()

n = int(first_multiple_input[0])
q = int(first_multiple_input[1])

queries = []

print("Enter the queries:")

for _ in range(q):
    queries.append(list(map(int, input().split())))

# Calculate result
result = dynamicArray(n, queries)

# Display result
print("Output:")

for answer in result:
    print(answer)