import mymenu
import stringlab
import stringutils


def is_palindrome(text: str) -> bool:
    normalized_text = stringutils.normalize(text)
    return normalized_text == normalized_text[::-1]


def main():
    while True:
        mymenu.print_menu()
        choice = mymenu.get_menu_choice()

        if choice == "1":
            user_input = input("Ange en sträng: ")
            if is_palindrome(user_input):
                print(f'"{user_input}" är ett palindrom.')
            else:
                print(f'"{user_input}" är inte ett palindrom.')

        elif choice == "2":
            text = input("Ange text: ")
            pattern = input("Ange mönster att markera: ")
            res = stringlab.highlight(text, pattern)
            print(f"Resultat: {res}")

        elif choice == "3":
            s1 = input("Ange första strängen: ")
            s2 = input("Ange andra strängen: ")
            if stringlab.is_anagram(s1, s2):
                print(f'"{s1}" och "{s2}" är anagram!')
            else:
                print(f'"{s1}" och "{s2}" är INTE anagram.')

        elif choice == "0":
            print("Avslutar programmet.")
            break
        else:
            print(f"Ogiltigt val: '{choice}'. Försök igen.")


if __name__ == "__main__":
    main()