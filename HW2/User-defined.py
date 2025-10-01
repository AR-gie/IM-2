def char_freq(text):
    freq = {}
    case_map = {}
    for letter in text:
        if letter.isalpha():
            key = letter.lower()
            if key not in freq:
                freq[key] = 1
                case_map[key] = letter
            else:
                freq[key] += 1
    result = {}
    for key in freq:
        result[case_map[key]] = freq[key]
    return result

enter = input("Enter string: ")

word_list = []

for word in enter.split(','):
    word_list.append(word.strip())

for word in word_list:
    ltr_counts = char_freq(word)
    for key in ltr_counts:
        value = ltr_counts[key]
        print(str(key) + "=" + str(value), end=", ")
    print()