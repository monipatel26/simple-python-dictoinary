'''
Title: language-translation-english-spanish
Author: Monika Patel
Purpose: Program to read a word from file and translate word
01 - read the file
02 - printed announcements
03 - checked whether the word is in dictionary
04 - asked user to if want to add the word
05 - defined the functions for adding and saving the word
06 - loopback to the transaltion
07 - stripped new lines
'''
file = open("translation.txt","a+")
file.seek(0)
def addWordPair(words, w1, w2):
    ''' appends a new word pair [w1,w2] to words
        words is a list representing the dictionary
        w1 and w2 are strings
    '''
    words[w1] = w2
    words[w2] = w1
def saveWordPair(filename, w1, w2):
    ''' appends a new word pair to the
        vocabulary file specified by filename
        filename, w1 and w2 are all strings
    '''
    filename.write('\n'+w1+' '+ w2)

print('-'*38)
print(f'{"Language Translation Program": ^38}')
print('-'*38)
colors =[]
for item in file.readlines():
    if item.strip() and (not item.startswith('#')):
            colors.append(item.split())
newColors = [n[::-1] for n in colors]
allColors = colors+newColors
dictionary = dict(allColors)
while True:
    word = input('\nEnter a word to translate: ')
    if word != '':
        if word in dictionary:
            print(word+" translates to "+dictionary[word])
        else:
            print(word+" is not in the dictionary.")
            while True:
                addWord = input("Would you like to add it? (y/n) ")
                if addWord == 'y':
                    translateNew = input("What does "+word+" translate to? ")
                    if(translateNew != ''):
                        addWordPair(dictionary, word, translateNew)
                        saveWordPair(file, word, translateNew)
                        print(word+" --> "+ translateNew+" has been added.")
                    else:
                        print(word + " is not added to the dictionary.")
                    break
                elif addWord == 'n':
                    print("OK. "+word+" will not be added.")
                    break
                else:
                    print("Please type y/n.")
    else:
        break
file.close()
