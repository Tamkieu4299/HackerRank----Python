#myself
n = int(input('Give me a number => ').strip())
if n % 2 != 0 or (n % 2 == 0 and n in range(6, 20)):
    print('weird')
if n % 2 == 0 and (n in  range(2, 5) or n > 20):
    print('not weird')
#another
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}
print(check[n%2==0 and (n in range(2,6) or n > 20)])