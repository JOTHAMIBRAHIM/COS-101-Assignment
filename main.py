import math

first_name = input("Please enter your name: ")

def calculate_vol_cylinder():
    radius = float(input('Please enter your radius '))
    height = float(input('Please enter the height '))
    result = 2 * math.pi * radius * height
    print(result)

def calculate_quadratic():
    equ_type = input('Is the equation in form a*x^2 + b*x + c = 0? (Y/N) ')
    if equ_type.upper()  == 'Y':
        a = float(input('Please enter the value of a: '))
        b = float(input('Please enter the value of b: '))
        c = float(input('Please enter the value of c: '))

        print(f'a = {a} | b = {b} | c = {c}')

        discriminant = (b ** 2) - (4 * a * c)

        if discriminant >= 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f'x1 = {x1} | x2 = {x2}')
        else:
            print("The equation has no real roots.")
    else:
        print("Invalid input or unsupported equation format.")

def calculate_power():
    workdone = float(input('Please enter the work done: '))
    time = float(input('Please enter the time: '))

    power = workdone / time
    print(f'Power = {power}')


def pythogoras_theorem():
    a = float(input('Please enter the a: '))
    b = float(input('Please enter the b: '))
    result = math.sqrt((a ** 2) + (b ** 2))
    print(f'The nth term of the arithmetic progression is {result}')


def gravitational_force():
    mass1 = float(input('Please enter the first term: '))
    mass2 = float(input('Please enter the second mass: '))
    radius = float(input('Please enter radius: '))


    G = 6.674 * (10 ** -11)
    force = G * (mass1 * mass2) / (radius ** 2)
    print(f'Gravitational force = {force}')

def main_menu():
        print("\nChoose an option from the following:")
        print("i) Calculate volume of a cylinder")
        print("ii) Calculate quadratic Equation")
        print("iii) Calculate Power")
        print("iv) Calculate Pythogoras Theorem")
        print("v) Calculate Gravitational force")


        choice = input("Enter your choice (i, ii, iii, iv, v): ").lower()

        if choice == 'i':
            calculate_vol_cylinder()
        elif choice == 'ii':
            calculate_quadratic()
        elif choice == 'iii':
            calculate_power()
        elif choice == 'iv':
            pythogoras_theorem()
        elif choice == 'v':
            gravitational_force()
        else:
            print("Invalid choice. Please select a valid option.")


main_menu()

print(f'Thank you {first_name} for participating in this quiz')
