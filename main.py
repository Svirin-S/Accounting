from application.db.people import get_employees
from application.salary import calculate_salary
import datetime
from PIL import Image

def main():
    print('ok')
a = calculate_salary()
b = get_employees()
dt_now = datetime.datetime.now()

if __name__ == '__main__':
    a
    b
    main()
    print(dt_now)
 