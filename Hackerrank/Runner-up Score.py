number_lst = []
for n in range(int(input('Your number of range => '))):
    number_ = int(input())
    number_lst.append(number_)
runner_up_score = sorted(list(set(number_lst)))[-2]
print(runner_up_score)
