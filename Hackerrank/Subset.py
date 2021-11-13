
#2
for i in range (int(input())):
    _, a = input(), set(input().split())
    _, b = input(), set(input().split())
    print(b.intersection(a) == a)
#3
for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))