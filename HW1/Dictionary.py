# Dictionary
mydict = {}
print("\nEnter how many rows and columns you want:")
rows = int(input("Enter row: "))
cols = int(input("Enter col: "))
print()

for r in range(rows):
    print(f"Row {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number {c+1} : "))
        mydict[(r, c)] = num

search_num = float(input("\nSearch: "))

print("\nThe numbers in the Dictionary are:\n")
for r in range (rows):
    for c in range (cols):
        print(f"{mydict[((r, c))]}", end=" ")
    print()

find_num = []
for key, value in mydict.items():
    if value == search_num:
        find_num.append(f"Row {key[0]+1}, Col {key[1]+1}")

if find_num:
    print(f"\nNumber {search_num} found at " + " and ".join(find_num))
else:
    print(f"\nNumber {search_num} not found in the Dictionary.")