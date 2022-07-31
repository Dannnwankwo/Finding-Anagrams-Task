# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    #Change words to their lowercase

    word = word.lower()
    anagram = anagram.lower()

    #Removing empty spaces

    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    return sorted(word) == sorted(anagram)

print("Anagram Status of 'Brush' and 'Shrub' is ", find_anagrams("Brush", "Shrub"))
print("Anagram Status of 'Edit' and 'Shrub is' ", find_anagrams("Edit", "Shrub"))
    
