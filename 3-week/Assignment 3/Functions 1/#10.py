
def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(get_unique_numbers( [20, 20, 30, 30, 40]))
# 20 30 40