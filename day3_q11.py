

#find the missing no in an array
list=list(map(int,input().split()))
k=sum(list)
n=int(input())
sum=0
for i in range(n+1):
     sum+=i
print(sum-k)