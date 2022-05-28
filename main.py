def find_anagram(word, anagram):
    word1 = list(word)
    word1.sort()
    anagram1 = list(anagram)
    anagram1.sort()
   
    return word1 == anagram1 

    
word = input('Enter word: ')    
anagram = input('Enter anagram: ')    
print(find_anagram( word, anagram ))