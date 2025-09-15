def converter(dollars):
    #peso-57.17 yen-146.67
    peso = dollars * 57.17
    yen = dollars * 146.67
    return peso, yen

sample = [59, 200, 500]
print("Enter currency in ($):", ", ".join((map(str, sample))))
print("\nDollar($)\t\tPhil Peso(P)\t\tJpn Yen(Y)")

for d in sample:
    peso, yen = converter(d)
    print(str(d) + "\t\t\t" + str(round(peso, 2)) + "\t\t\t" + str(round(yen, 2)))