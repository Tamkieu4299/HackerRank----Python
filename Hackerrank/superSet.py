#1
a = set(input().split())
counter , n = 0, int(input())
for i in range (n):
        b = set(input().split())
        if a.issuperset(b) :
                counter += 1
print(counter == n)

#2
a=set(map(int, input().split()))
n=input()
f=0
for i in range(n):
    b=set(map(int, input().split()))
    if len(b.difference(a))!=0:
        f=1
    else:
        if len(b)==len(a):
            f=1
if f==0:
    print("True")
else:
    print ("False")