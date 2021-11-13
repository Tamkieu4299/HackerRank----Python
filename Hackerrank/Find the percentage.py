#myself
total_marks = []
total_names = []
for i in range(int(input('Number of student => '))):
    stu_name = input()
    one_stu_marks_lst = list((input().split()))
    total_marks.append([*one_stu_marks_lst])
    total_names.append(stu_name.title())
student_ = input("What's student you want to see => ")
student_ind = total_names.index(student_)
get_marks = total_marks[student_ind]
int_get_marks = list(map(int, get_marks))
print(student_, ':', "{:.2f}".format(sum(int_get_marks)/ len(int_get_marks)))

#their method
n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
print(student_marks)
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))



