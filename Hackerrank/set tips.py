n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    # use eval() to conduct the function
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))