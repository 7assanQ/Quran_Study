'''
To count how many each letter is repeated in the Quran

'''

from collections import Counter

letters = []
total = 0

file_path = "Quran.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("|")
        for letter in parts[2]:
            letters.append(letter)

print('\nNumber of how many each letter in the Quran is repeted')
letter_counts = Counter(letters)
for letter, count in letter_counts.items():
    total += count
    print(f"The letter  {letter}  is repeated {count} times.\n")

print(total)    