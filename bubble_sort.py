file = open("./list-1.txt")
list = []
for i in file.readlines():
    try:
        list.append(int(i))
    except ValueError:
        continue
print(f"Unorganized list: {list}\n\n")
for vals in range(len(list) - 1):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            temp = list[i + 1]
            list[i + 1] = list[i]
            list[i] = temp
print(f"Organized List: {list}\n\n")


# Notes
"""
For 15 Elements it is near instantaneous

"""
