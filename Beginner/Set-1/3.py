inp = input()

vowels = ["a","e","i","o","u"]

if inp in vowels:
    print("Vowel")
elif inp not in vowels:
    print("Consonant")
else:
    print("Invalid Input")