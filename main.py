if __name__ == "__main__":
    print("Программа калькулятора")
    while True:
        chose = input("считаем или выходим").strip().lower()
        if chose == "считаем":
            vyrazhenie = input("Введите выражение: ")
        elif chose == "выходим":
            break
    print("досвидания")