'''
to read the content of the ayat based
on the givin surah number and the ayat number

'''
######### USER INPUT #########

surah = "12"
ayat = "93"

##############################

import arabic_reshaper
from bidi.algorithm import get_display

file_path = "Quran.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("|")
            
        if parts[0] == surah and parts[1] == ayat:

            reshaped_text = arabic_reshaper.reshape(parts[2])
            bidi_text = get_display(reshaped_text)

            print(f"surah: {parts[0]}")
            print(f"ayat: {parts[1]}")
            print(f"Content: {bidi_text}")
            break
