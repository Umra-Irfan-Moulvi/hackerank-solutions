def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    minutes_seconds = s[2:8]

    if period == "AM":
        if hour == 12:
            hour = 0

    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02d}{minutes_seconds}"


# Take input
s = input("Enter time in 12-hour format: ")

# Convert time
result = timeConversion(s)

# Display result
print("24-hour format:", result)