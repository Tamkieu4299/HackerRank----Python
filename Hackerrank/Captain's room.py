#my solution
a = int(input())
number_array = list(map(int,input().split()))
def recur_captain(number_array):
    if number_array[len(number_array) - 1] not in number_array[(len(number_array) - 2): 0 : -1]:
        return number_array[len(number_array) -1]
    else:
        return recur_captain(number_array[len(number_array) - 1 : 0 : -1])
print(recur_captain(number_array))

#their solution
k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))

#Their solution
_ = input()
a = input().split()
s = set()
t = set()
for i in a:
    if i not in s:
        s.add(i)
        t.add(i)
    else:
        t.discard(i)
print(t.pop())