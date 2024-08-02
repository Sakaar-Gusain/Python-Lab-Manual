rows = 3  # Number of rows in the diamond

# Upper half of the diamond
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '* ' * i)