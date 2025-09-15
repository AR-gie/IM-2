def char_freq(text):
    freq = {}
    for c in text:
        if c != ",":
            freq[c] = freq.get(c, 0) + 1
    return freq

sample = ["Philippines", "Hello", "Wakawaka"]
print("Enter string: " + ", ".join(sample))
print()

for word in sample:
    result = char_freq(word)
    for c, count in result.items():
        print(f"{c}={count}")
    print()