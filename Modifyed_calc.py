while True:

    first_number= int(input("Введіть перше число: "))
    operation = input("Введіть дію (+, -, *, /): ")
    second_number = int(input("Введіть друге число: "))


    if operation == '+':
        result = first_number + second_number
        print("Результат:", result )
    elif operation == '-':
        result = first_number - second_number
        print("Результат:", result)
    elif operation == '*':
        result = first_number * second_number
        print("Результат: ", result)
    elif operation == '/':
        if second_number == 0:
            print("Ділити на нуль не можна!")
        else:
            result = first_number / second_number
            print("Результат: ", result)

    print()
    print()


    print("Помилка: невідома операція!")


    choice = input("Бажаєте продовжити? (y/no): ")
    if choice == 'y':
        print("Програма завершена.")
        break
    elif choice == 'no':
        break