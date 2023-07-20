#Binary Search

num=int(input("Enter Number of Elements: "))
arr=[]
for i in range(num):
    a=int(input("Enter Element: "))
    arr.append(a)
target=int(input("Enter Element to Search: "))
arr.sort()
low=0
high=len(arr)
mid=(low + high)//2
while high>=mid:
    if target==arr[mid]:
        print(f"Element found in {mid+1} position")
    if target>arr[mid]:
        low=mid+1
    if target<arr[mid]:
        high=mid-1
    mid=(low + high)//2