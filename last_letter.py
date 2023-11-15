'''
To read the last letters in the surah
and count how many of them occurred

'''
######### USER INPUT #########

surah = "12"

##############################

from collections import Counter

all_last_letters = []
i = 1

file_path = "Quran.txt"
print('Last letter at')

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("|")
            
        if parts[0] == surah:
            last_letter = line.strip()[-2]
            all_last_letters.append(last_letter)
            print(f"ayat {i}: {last_letter}")
            i += 1

print('\nNumber of how many each letter at the end of each ayat is repeted')
letter_counts = Counter(all_last_letters)
for letter, count in letter_counts.items():
    print(f"The letter  {letter}  is repeated {count} times.\n")