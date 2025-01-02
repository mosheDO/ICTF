# coding: utf-8
def find_letter (curr_letter):
    alphabet = set(string.ascii_uppercase)
    found_letters = set()
    with open('./output.txt', 'r') as f:
        for line in f:
            char = line[curr_letter].upper()
            found_letters.add(char)
    missing_letters = alphabet - found_letters
    if len(missing_letters) > 1:
        print(line[curr_letter], end='')
    else:
        print (list(missing_letters)[0], end='')

for i in range(25):
    find_letter(i)
    
