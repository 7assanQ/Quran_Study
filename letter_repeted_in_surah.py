'''
To count how many each letter is repeated in the surah

'''
######### USER INPUT #########

surah = "12"

##############################

from collections import Counter

letters = []

file_path = "Quran.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("|")
            
        if parts[0] == surah:
            for letter in parts[2]:
                letters.append(letter)

print('\nNumber of how many each letter in the surah is repeted')
letter_counts = Counter(letters)
for letter, count in letter_counts.items():
    print(f"The letter  {letter}  is repeated {count} times.\n")