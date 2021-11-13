n,m = map(int,input().split())
N = list(map(int,input().split()))
A = list(set(map(int,input().split())))
B = list(set(map(int,input().split())))
like_lst = list(set(N + A))
dislike_lst = list(set(N + B))
grade_ = len(like_lst) - len(dislike_lst)
print(abs(grade_))


#their solution
n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print (sum([(i in A) - (i in B) for i in sc_ar]))