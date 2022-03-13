from num2words import num2words


def math ():
    countwhile = 0
    accept = "y"
    counter = 0
    while accept == "y":
        countwhile += 1
        number1 = input(" введите первое число:")
        if number1 == "stop":
            break
        operation = input(" введите арифметический оператор:")
        if operation == " stop":
            break
        number2 = input(" введите второе число:")
        if number2 == " stop":
            break

        try:
            if operation == "+":
                counter = float(number1) + float(number2)
                print(" сумма чисел равна: " + num2words(counter, lang = 'ru'))

            if operation == "-":
                counter = float(number1) - float(number2)
                print(" разность чисел равна: " + num2words(counter, lang = 'ru'))

            if operation == "*":
                counter = float(number1) * float(number2)
                print(" произведение чисел равно: " + num2words(counter, lang = 'ru'))
            try:
                if operation == "/":
                    counter = float(number1) / float(number2)
                    print(" частное из чисел: " + num2words(counter, lang = 'ru'))
            except ZeroDivisionError:
                print(" https://elementy.ru/email/1530320/Pochemu_nelzya_delit_na_nol")
                math()

            if operation == "%":
                counter = float(number1) % float(number2)
                print(" остаток от деления: " + num2words(counter, lang = 'ru'))

            if operation == "**":
                counter = float(number1) ** float(number2)
                print(" результат возведения числа ", number1, "в степень", number2, ": " +num2words(counter,lang = 'ru'))
        except ValueError:
            print("Введен неправильный аргумент (первое или второе число)")
            math()

        print(" Количество совершенных операций : "+str(countwhile))
        accept = input(" Желаете продолжить? (y/n) \n : ")
        if accept == "y":
            continue
        if accept == "n":
            print (" Всего наилучшего!")
            break
        if accept != "y" or "n":
            print(" Неправильный аргумент, инициализирован повторный цикл")
            accept = "y"