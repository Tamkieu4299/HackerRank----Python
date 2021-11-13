#myself
n = int(input())
for i in  range(0, n):
    print(i ** 2)
#another
n = int(input())
print(*[num**2 for num in range(n)], sep='\n')
