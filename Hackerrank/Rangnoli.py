#Use String ascii
import string
alpha = string.ascii_lowercase
print(alpha)
n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(s)
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print(L)
print('\n'.join(L[:0:-1]+L))

#use function
def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    print(myStr)
    for i in range(size - 1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1] + myStr[x:size]
            print(line)
            print("--" * x + '-'.join(line) + "--" * x)