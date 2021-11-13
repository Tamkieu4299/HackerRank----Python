#myself
def is_leap(year):
    if (year % 4 == 0 and year % 100 == 0 and year % 400 ==0) or (year % 4 == 0 and year % 100 != 0):
            return True
    else:
            return False
#another
def iss_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
year_ = int(input("Enter a year => "))
check_year = iss_leap(year_)
print(check_year)
