def print_menu():
    print("\n--- MENY ---")
    print("1. Kontrollera palindrom")
    print("2. Markera mönster")
    print("3. Kontrollera anagram")
    print("0. Avsluta")


def get_menu_choice() -> str:
    return input("Välj ett alternativ: ")