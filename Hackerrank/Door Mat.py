#Myself
n = int(input("N = "))
m = n * 3
shape_ = ".|."
center_= "HANGTAM"
list_ = []
for i in range(1, n + 1, 1):
    a = i - 1
    if i < (n + 1)/2:
        row_1 = " ".ljust(int((m-(3*(i+a)))/2) + 1, '-') + ((i+a) * shape_).ljust((3 * (i + a)), " ") + " ".ljust(int((m -(3*(i+a)))/2) + 1, '-').strip()
        print(row_1)
        list_.append(row_1)
        continue
    if i == (n + 1) /2:
        row_2 = " ".ljust(int((m-7)/2) + 1, '-') + center_.ljust(7, " ") + " ".ljust(int((m-7)/2) + 1, '-').strip()
        print(row_2)
        continue
    if i > (n + 1) /2:
        row_3 = list_[n - i]
        print(row_3)
        print(list_)

#Their solution
if __name__ == '__main__':
        N, M = map(int, input().split(" "))

        for i in range(N):
                pattern = ".|."
                if i < (N-1)/2:
                        print((pattern * (2*i+1)).center(M, "-"))
                elif i == (N-1)/2:
                        print("WELCOME".center(M, "-"))
                else:
                        print((pattern * (2*(N-1-i)+1)).center(M, "-"))