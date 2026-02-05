# Filter only names that start with the letter "p"

names = ["Patrick", "Paul", "Jonhny", "Rose", "Ana"]

names_begin_letter_P = list(
    filter(lambda p: p.startswith("P"), names))

print(names_begin_letter_P)