file = open("./list-1.txt")
list = []
for i in file.readlines():
    try:
        list.append(int(i))
    except ValueError:
        continue
print(f"Unorganized list: {list}")
for vals in range(len(list) - 1):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            temp = list[i + 1]
            list[i + 1] = list[i]
            list[i] = temp
print(list)


# Notes
"""
For 15 Elements it is near instantaneous

"""
