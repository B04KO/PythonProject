def is_palindrome(text):
    text = text.replace(" ", "").lower()

    return text == text[::-1]

user_input = input("Введите слово или фразу: ")

if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
