day = 1
total_bugs = 0

while day <= 5:
    bugs = int(input("please enter the amount of bugs collected today"))
    total_bugs = bugs + total_bugs
    print(total_bugs)
    day = day + 1
