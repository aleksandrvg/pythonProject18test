def isValidInput(string: str):
    if string.find("+") != -1 or string.find("-") != -1 or string.find("*") != -1 or string.find(":") != -1:
        if string.count("+") <= 1 or string.count("-") <= 1 or string.count("*") <= 1 or string.count(":") <= 1:
            return True
        else:
            return False
    else:
        return False
def calculate(string: str, sign: str):
    try:
        num1 = float(string[:string.find(sign)])
        num2 = float(string[string.find(sign)+1:])
        rez = 0
        if sign == "+":
            rez = num1 + num2
        elif sign == "-":
            rez = num1 - num2
        elif sign == "*":
            rez = num1 * num2
        elif sign == ":":
            rez = num1 / num2
        return rez
    except:
        print("Ошибка проверьте выражение")
if __name__ == "__main__":
    print("Программа калькулятора")
    while True:
        chose = input("считаем или выходим").strip().lower()
        if chose == "считаем":
            vyrazhenie = input("Введите выражение: ")
            if isValidInput(vyrazhenie):
                pass
            else:
                print("Некорректный формат")
                continue
        elif chose == "выходим":
            break
    print("досвидания")