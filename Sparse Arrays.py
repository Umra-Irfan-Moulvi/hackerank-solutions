def matchingStrings(stringList, queries):
    frequency = {}

    # Count how many times each string appears
    for string in stringList:
        if string in frequency:
            frequency[string] += 1
        else:
            frequency[string] = 1

    result = []

    # Find the frequency of each query
    for query in queries:
        result.append(frequency.get(query, 0))

    return result


# Take input
stringList_count = int(input("Enter number of strings: "))

stringList = []

for _ in range(stringList_count):
    stringList.append(input())


queries_count = int(input("Enter number of queries: "))

queries = []

for _ in range(queries_count):
    queries.append(input())


# Calculate result
result = matchingStrings(stringList, queries)


# Display result
print("Output:")

for answer in result:
    print(answer)