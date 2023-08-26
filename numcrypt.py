import re
print("""
🔐 Numcrypt
""")

def text_to_numbers(text):
    result = []
    for char in text:
        if char.isalpha():
            num = ord(char.lower()) - ord('a') + 1
            result.append(f"[{num}]")
        else:
            result.append(char)
    return ''.join(result)

input_text = input("ENCRYPT>")
converted_text = text_to_numbers(input_text)
print(converted_text)


def numbers_to_text(numbers_text):
    def replace(match):
        num = int(match.group(1))
        char = chr(num - 1 + ord('a'))
        return char

    decrypted_text = re.sub(r'\[(\d+)\]', replace, numbers_text)
    return decrypted_text


numbers_text = input("DECRYPT>")
original_text = numbers_to_text(numbers_text)
print(original_text)
input("Enter to exit")