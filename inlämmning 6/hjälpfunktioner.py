def verify_action(prompt: str) -> bool:
    """Frågar användaren om bekräftelse (Ja/Nej)."""
    while True:
        answer = input(f"{prompt} (j/n): ").strip().lower()
        if answer in ['j', 'ja']:
            return True
        elif answer in ['n', 'nej']:
            return False
        print("Svara med 'j' för ja eller 'n' för nej.")


def get_non_empty_input(prompt: str) -> str:
    """Säkerställer att användaren inte matar in ett tomt värde."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Inmatningen får inte vara tom. Försök igen.")