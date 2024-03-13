rows = int(input("Enter the number of rows: "))

# Printing upper half of the pattern
for i in range(1, rows + 1):
    print("* " * i)

# Printing lower half of the pattern
for i in range(rows - 1, 0, -1):
    print("* " * i)
