import mymenu
import stringutils

def is_palindrome(text: str) -> bool:
    normalized_text = stringutils.normalize(text)
    return normalized_text == normalized_text[::-1]

def highlight(text: str, pattern: str) -> str:
    if not pattern:
        return text
    return text.replace(pattern, f"({pattern})")

def is_anagram(string_1: str, string_2: str) -> bool:
    clean_1 = sorted(c.lower() for c in string_1 if c.isalpha())
    clean_2 = sorted(c.lower() for c in string_2 if c.isalpha())
    return clean_1 == clean_2
    
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
        elif choice == "0":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()