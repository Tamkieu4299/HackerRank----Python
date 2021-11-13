def merge_the_tool(string, k):
    for i in range(0, len(string), k):
        char_lst = []
        slice_str = string[i:i + k]
        for x in slice_str:
            if x not in char_lst:
                char_lst.append(x)
        print(''.join(char_lst))
merge_the_tool(string="AABCAAADA", k=3)

#Their solution
S, N = input(), int(input())
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


#another
from collections import OrderedDict

def merge_the_tools(string, k):
    for x in range(0,len(string),k):
        print(''.join(list(OrderedDict.fromkeys(string[x:x+k]))))