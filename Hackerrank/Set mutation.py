(_, A) = (int(input()),set(map(int, input().split())))
B = int(input())
for _ in range(B):
    (command, newSet) = (input().split()[0],set(map(int, input().split())))
    getattr(A, command)(newSet)
print(sum(A))


#my method
n1 = int(input())
A = set(map(int, input().split()))
n2 = int(input())
for i in range(n2):
    opr_name, element_ = input().split()
    another_set = set(map(int, input().split()))
    eval('A.{}({})'.format(opr_name, another_set))
print(sum(list(A)))