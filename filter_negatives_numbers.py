#filter negative numbers

values= [0, 1, -1, 2, -2, 3, -3]
negative_values = list(filter(lambda n: n < 0, values))
print(negative_values)
