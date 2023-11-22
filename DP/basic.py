def print_name_five_times(i, n):
    for n in range(i, n):
        print("Nishant Bhickta")
        print_name_five_times(i+1, n-1)

print_name_five_times(0, 5)