"""
Zachary Bedrosian
Session 9 Exercises
10.03.2017
"""


# Exercise 2

# 2.1 Rewrite is_abecedarian using recursion

def is_abecedarian_recursion(word, letter_count=0):
    current_letter = word[letter_count]
    if (letter_count != len(word) -1):
        if current_letter == word[letter_count + 1]:
            print('The letter ' + current_letter + ' repeats.')
            return True
        else:
            is_abecedarian_recursion(word, letter_count+1)
    else:
        print('No Letters Match In This Word')
        return False
    
is_abecedarian_recursion('Zacharyy')

# 2.2 Rewrite is_abecedarian using while loop.

def is_abecedarian_while(word):
    letter_count = 0
    while letter_count != (len(word) -1):
        current_letter = word[letter_count]
        if current_letter == word[letter_count + 1]:
            print('The letter ' + current_letter + ' repeats.')
            return True
        else:
            letter_count += 1

    print('No Letters Match In This Word')
    return False

is_abecedarian_while('Zacharyy')

# Exercise 3
"""
Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify,
but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that
sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work.
But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may
be the only word. Of course there are probably 500 more but I can only think of one. What is the word? 
"""

def find_the_letter_triplets_helper(word, letter_count=0):
    current_letter = word[letter_count]
    if (letter_count != len(word) -2):
        if current_letter == word[letter_count + 1] and current_letter == word[letter_count + 2]:
            print('In the word "' + word + '" the letter "' + current_letter.title() + '" repeats 3 times.')
            return True
        else:
            find_the_letter_triplets_helper(word, letter_count+1)
    else:
        return False
    

def find_the_letter_triplets():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        find_the_letter_triplets_helper(word)

find_the_letter_triplets()