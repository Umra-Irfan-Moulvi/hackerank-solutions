def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return [alice, bob]


# Take input
a = list(map(int, input("Enter Alice's scores: ").split()))
b = list(map(int, input("Enter Bob's scores: ").split()))

# Calculate result
result = compareTriplets(a, b)

# Display result
print("Alice's score:", result[0])
print("Bob's score:", result[1])