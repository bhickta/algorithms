def print_name_five_times(n):
    for n in range(n):
        print("Nishant Bhickta")
        print_name_five_times(n - 1)

print_name_five_times(2)