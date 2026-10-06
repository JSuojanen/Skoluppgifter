from hjälpfunktioner import verify_action, get_non_empty_input

# HANTERING AV PERSONER
def add_person(directory: dict):
    """Lägger till en ny person i katalogen."""
    print("\n--- LÄGG TILL PERSON ---")
    name = get_non_empty_input("Ange namn på personen: ").capitalize()

    if name in directory:
        print(f"Personen '{name}' finns redan i katalogen.")
        return

    directory[name] = {}
    print(f"'{name}' har lagts till i katalogen.")

    if verify_action("Vill du lägga till ett telefonnummer direkt?"):
        add_number_to_person(directory, name)


def remove_person(directory: dict):
    """Tar bort en person från katalogen efter bekräftelse."""
    print("\n--- TA BORT PERSON ---")
    name = get_non_empty_input("Ange namn på personen du vill ta bort: ").capitalize()

    if name not in directory:
        print(f"Kunde inte hitta '{name}' i katalogen.")
        return

    if verify_action(f"Är du säker på att du vill ta bort '{name}' och alla tillhörande nummer?"):
        del directory[name]
        print(f"'{name}' har tagits bort från katalogen.")
    else:
        print("Åtgärden avbröts.")


def list_all_persons(directory: dict):
    """Visar en lista med endast namnen på alla personer i katalogen."""
    print("\n--- PERSONER I KATALOGEN ---")
    if not directory:
        print("Katalogen är tom.")
        return

    for index, name in enumerate(sorted(directory.keys()), start=1):
        print(f"{index}. {name}")


def search_person(directory: dict):
    """Söker efter en person och visar dennes telefonnummer."""
    print("\n--- SÖK PERSON ---")
    name = get_non_empty_input("Ange namn att söka efter: ").capitalize()

    if name not in directory:
        print(f"Kunde inte hitta '{name}' i katalogen.")
        return

    numbers = directory[name]
    print(f"\nKontaktkort för {name}:")
    if not numbers:
        print("  Inga telefonnummer registrerade.")
    else:
        for category, number in numbers.items():
            print(f"  • {category.capitalize()}: {number}")

# HANTERING AV TELEFONNUMMER

def add_number_to_person(directory: dict, target_name: str = None):
    """Lägger till ett nytt nummer för en specifik eller angiven person."""
    if not target_name:
        print("\n--- LÄGG TILL NUMMER ---")
        target_name = get_non_empty_input("Ange namn på personen: ").capitalize()

    if target_name not in directory:
        print(f"Kunde inte hitta '{target_name}'. Skapa personen först.")
        return

    category = get_non_empty_input("Ange kategori (t.ex. mobil, hem, jobb): ").lower()

    if category in directory[target_name]:
        print(f"Det finns redan ett nummer registrerat under kategorin '{category}'.")
        print("Använd alternativet 'Uppdatera nummer' om du vill ändra det.")
        return

    number = get_non_empty_input("Ange telefonnummer: ")
    directory[target_name][category] = number
    print(f"Numret '{number}' ({category}) har lagts till för {target_name}.")


def remove_number(directory: dict):
    """Tar bort ett specifikt nummer för en person efter bekräftelse."""
    print("\n--- TA BORT NUMMER ---")
    name = get_non_empty_input("Ange namn på personen: ").capitalize()

    if name not in directory:
        print(f"Kunde inte hitta '{name}' i katalogen.")
        return

    if not directory[name]:
        print(f"'{name}' har inga registrerade nummer.")
        return

    print(f"Tillgängliga kategorier för {name}: {', '.join(directory[name].keys())}")
    category = get_non_empty_input("Ange kategori att ta bort: ").lower()

    if category not in directory[name]:
        print(f"Kategorin '{category}' hittades inte för {name}.")
        return

    if verify_action(f"Vill du ta bort numret under '{category}' för {name}?"):
        del directory[name][category]
        print(f"Kategorin '{category}' har tagits bort för {name}.")
        if not directory[name]:
            print(f"Märk: {name} har nu inga nummer kvar i katalogen.")
    else:
        print("Åtgärden avbröts.")


def update_number(directory: dict):
    """Uppdaterar ett befintligt nummer för en viss person."""
    print("\n--- UPPDATERA NUMMER ---")
    name = get_non_empty_input("Ange namn på personen: ").capitalize()

    if name not in directory:
        print(f"Kunde inte hitta '{name}' i katalogen.")
        return

    if not directory[name]:
        print(f"'{name}' har inga registrerade nummer att uppdatera.")
        return

    print(f"Tillgängliga kategorier för {name}: {', '.join(directory[name].keys())}")
    category = get_non_empty_input("Ange kategori att uppdatera: ").lower()

    if category not in directory[name]:
        print(f"Kategorin '{category}' finns inte. Använd 'Lägg till nummer' för att skapa ny kategori.")
        return

    current_number = directory[name][category]
    print(f"Nuvarande nummer ({category}): {current_number}")
    new_number = get_non_empty_input("Ange nytt telefonnummer: ")

    if verify_action(f"Vill du ersätta '{current_number}' med '{new_number}'?"):
        directory[name][category] = new_number
        print("Numret har uppdaterats.")
    else:
        print("Åtgärden avbröts.")