def grade(data):
    if 2.00 <= data <= 2.99:
        print('Fail')
    elif 3.00 <= data <= 3.49:
        print('Poor')
    elif 3.50 <= data <= 4.49:
        print('Good')
    elif 4.50 <= data <= 5.49:
        print('Very Good')
    elif data >= 5.50:
        print('Excellent')


grade_data = float(input())

grade(grade_data)