import  turtle
from turtle import *


# Function definition
def draw_pie_chart(staff_id, normal_hour_salary, night_shift_salary, overtime_salary, overtime_night_shift_salary,
                   holiday_salary, supporting_fee):
    """ Get tam to draw a pie chart of percent_. Where 1% = 3.6 degree """
    total_payment = normal_hour_salary + night_shift_salary + overtime_salary + overtime_night_shift_salary + holiday_salary + supporting_fee
    color_ = ["red", "blue", "hotpink", "yellow", "grey", "black"]

    lst_of_payment_categories = [normal_hour_salary, night_shift_salary, overtime_salary, overtime_night_shift_salary,
                                 holiday_salary, supporting_fee]
    # return lst_of_payment_categories, total_payment, staff_id

    # Draw pie chart
    staff_id.penup()
    staff_id.forward(100)
    staff_id.left(90)
    staff_id.pendown()
    staff_id.circle(100)
    color_ = ["red", "blue", "hotpink", "yellow", "grey", "black"]
    percent_plus = 0
    staff_id.heading()
    #heading_origin = 0
    percent_0 = (lst_of_payment_categories[0] / total_payment) * float(100) * float(3.6)  # 1% = 3.6 degree
    staff_id.fillcolor(color_[0])
    heading_origin = staff_id.heading()
    percent_plus += percent_0
    # staff_id.setheading(percent_plus)
    # staff_id.pendown()
    staff_id.begin_fill()
    # staff_id.forward(100)
    staff_id.circle(100, percent_0)
    staff_id.goto(0, 0)
    staff_id.penup()
    staff_id.setheading(percent_plus)
    staff_id.right(percent_0)
    staff_id.forward(100)
    staff_id.end_fill()
    staff_id.left(heading_origin)
    staff_id.circle(100, percent_0)

    percent_plus_1 = percent_plus
    percent_1 = (lst_of_payment_categories[1] / total_payment) * float(100) * float(3.6)  # 1% = 3.6 degree
    staff_id.fillcolor(color_[1])
    heading_origin_1 = staff_id.heading()
    percent_plus_1 += percent_1
    # staff_id.setheading(percent_plus)
    # staff_id.pendown()
    staff_id.begin_fill()
    # staff_id.forward(100)
    staff_id.circle(100, percent_1)
    staff_id.goto(0, 0)
    staff_id.penup()
    staff_id.setheading(percent_plus)
    staff_id.right(percent_1)
    staff_id.forward(100)
    staff_id.end_fill()
    staff_id.left(heading_origin_1)
    staff_id.circle(100, percent_1)


win = turtle.Screen()
win.bgcolor("Lightgreen")
win.title("Pie Chart")
id111 = turtle.Turtle()
id111.color("White")
id111.pensize(3)

draw_pie_chart(id111, 1, 1, 1, 1, 1, 1)

win.exitonclick()