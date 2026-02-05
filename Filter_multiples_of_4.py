# Filter multiples of 4

numbers = list(range(1, 101))

multiples_4 = list(
    filter(lambda m: m % 4 == 0, numbers)
)

print(multiples_4)