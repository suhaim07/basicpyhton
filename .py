year = int(input("enter the year: "))

leap_year = 2024

if (leap_year - year) % 4 == 0 :
    print("it is leap year")
else:
    print("not leap year")