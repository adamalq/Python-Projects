numbers = [4, 7, 2, 7, 9, 4, 12, 9]
unique_numbers = list(set(numbers))
max_value = max(unique_numbers)
print(f"Maximum value: {max_value},remove max value: {unique_numbers.remove(max_value)}")
Secondmax_value = max(unique_numbers)
print(f"Second maximum value: {Secondmax_value}")