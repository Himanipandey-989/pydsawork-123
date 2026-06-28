n=int(input("enter thr value of number:" ))
count=0
while n>0:
  last_digit=n%10
  count=count+1
  n=n//10
print(count)

