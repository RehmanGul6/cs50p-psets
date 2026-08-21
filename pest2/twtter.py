user_input = input("input: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

for char in user_input:
    if char in vowels:
        continue
    print(char, end="")