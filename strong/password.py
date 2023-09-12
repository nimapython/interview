import random

def generate_random_password(hint_word):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "{}[]();'*#.<>_!"
    all = hint_word + lower + upper + digits + symbols
    length = 12
    password = "".join(random.sample(all, length))
    return password

hint_word=input("Enter a hint word:")
print("The Generated Password is:",generate_random_password(hint_word))



