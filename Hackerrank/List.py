#myself
number_lst = []
for n in range(int(input('How many commands you want => '))):
    one_cmd = input().strip().lower()
    if one_cmd == "insert":
        eval("number_lst.insert({0},{1})".format(int(input("what's INDEX => ")), int(input("what's NUMBER => "))))
    elif one_cmd == "append" or one_cmd == "remove":
        eval("number_lst.{0}({1})".format(one_cmd, eval(input("what's NUMBER => "))))
    elif one_cmd == "print":
        print(number_lst)
    else:
        eval("number_lst.{0}()".format(one_cmd))


#their solution
L = []
for _ in range(0, int(input())):
    user_input = input().split(' ') #user inputs append 2
    command = user_input.pop(0) #get 'append'
    if len(user_input) > 0:
        if 'insert' == command:
            eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
        else:
            eval("L.{0}({1})".format(command, user_input[0]))
    elif command == 'print':
        print (L)
    else:
        eval("L.{0}()".format(command))





