
from katalog import (
    list_all_persons,
    search_person,
    add_person,
    remove_person,
    add_number_to_person,
    remove_number,
    update_number
)

# Startdata enligt uppgiftsbeskrivningen
directory = {
    "Anna": {
        "mobil": "0457123456",
        "hem": "01812345"
    },
    "Bertil": {
        "jobb": "04001998877"
    },
    "Cecilia": {
        "mobil": "+46701234567",
        "föglö": "01854321"
    }
}


def display_menu():
    """Skriver ut huvudmenyn."""
    print("\n========================================")
    print("           TELEFONKATALOG")
    print("========================================")
    print("1. Visa alla personer (endast namn)")
    print("2. Sök efter person och visa nummer")
    print("3. Lägg till person")
    print("4. Ta bort person")
    print("----------------------------------------")
    print("5. Lägg till nummer för en person")
    print("6. Ta bort nummer för en person")
    print("7. Uppdatera nummer för en person")
    print("----------------------------------------")
    print("0. Avsluta programmet")
    print("========================================")


def main():
    """Huvudloop för programmet."""
    while True:
        display_menu()
        choice = input("Välj ett alternativ (0-7): ").strip()

        if choice == "1":
            list_all_persons(directory)
        elif choice == "2":
            search_person(directory)
        elif choice == "3":
            add_person(directory)
        elif choice == "4":
            remove_person(directory)
        elif choice == "5":
            add_number_to_person(directory)
        elif choice == "6":
            remove_number(directory)
        elif choice == "7":
            update_number(directory)
        elif choice == "0":
            print("\nTack för att du använde telefonkatalogen. Hej då!")
            break
        else:
            print("\n[FEL] Ogiltigt val! Skriv en siffra mellan 0 och 7.")


if __name__ == "__main__":
    main()