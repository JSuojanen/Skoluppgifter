def normalize(text: str) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            result += char.lower()
    return result