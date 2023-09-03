import roman


def main():
    try:
        user_input = input("Tam sayıya çevirmek istediğiniz roma rakamını giriniz. >> ")
        print(roman.fromRoman(user_input))
    except roman.InvalidRomanNumeralError:
        print("Geçersiz roman rakamı.")


if __name__ == "__main__":
    main()
