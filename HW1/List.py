# List
mylist = []
print("\nEnter how many rows and columns you want:")
rows = int(input("Enter row: "))
cols = int(input("Enter col: "))
print()

for r in range(rows):
    print(f"Row {r+1}")
    row_list = []
    for c in range(cols):
        num = float(input(f"Enter number {c+1} : "))
        row_list.append(num)
    mylist.append(row_list)

search_num = float(input("\nSearch: "))

print("\nThe numbers in the List are:\n")
for r in range (rows):
    for c in range (cols):
        print(f"{mylist[r][c]}", end=" ")
    print()

find_num = []
for r in range(rows):
    for c in range(cols):
        if mylist[r][c] == search_num:
            find_num.append(f"Row {r+1}, Col {c+1}")

if find_num:
    print(f"\nNumber {search_num} found at " + " and ".join(find_num))
else:
    print(f"\nNumber {search_num} not found in the List.")