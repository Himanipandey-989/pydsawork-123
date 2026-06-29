arr=list(map(int,input("enter space dekar likhein: ").split()))
left=0
for i in range(len(arr)):
  if arr[i]!=0:
    arr[left],arr[i]=arr[i],arr[left]
    left=left+1
print (arr)