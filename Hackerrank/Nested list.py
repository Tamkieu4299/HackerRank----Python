d={} #1 Emty Dictionary
for _ in range(int(input())): #2 Range for number of students.
    Name=input() #3  Accepting name of the student.
    Grade=float(input()) #4 Accepting the grade of the student.
    d[Name]=Grade #5 Assigning name as key and grade as value for the dictionary.
v=d.values()#6  Obtaining the values of dictionary(all grades of students).
second=sorted(list(set(v)))[1] #7 Removing duplicte grades by using set data type , changing it to list, sorting in ascending order and taking the second lowest grade.
second_lowest=[] #8  Declaring an empty list for storing the name of the students who got the second lowest grade.
for key,value in d.items():  #9 Going through the name and grade of each students by using items() method of dictionary.
    if value==second: #10  Checking whether the grade is equal to the second lowest grade.
        second_lowest.append(key) #11  If yes , append it to the second_lowest list.
second_lowest.sort() #12 Sorting the name of students in asceding order
for name in second_lowest: #13 Going through the name of each students who got the second lowes grade.
    print(name) #14 Printing each name of students in seperate line.


























