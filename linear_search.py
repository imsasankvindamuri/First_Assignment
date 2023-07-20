#Linear Search

num=int(input("Enter Number of Elements: "))
arr=[]
for i in range(num):
    a=int(input("Enter Element: "))
    arr.append(a)
target=int(input("Enter Element to Search: "))
dupe=0

for i in range(len(arr)):
    if int(arr[i])==target:
        print(f"Found in position {i}")
        dupe+=1
if dupe==0:
    print("Not Found")