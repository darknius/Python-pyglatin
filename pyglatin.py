#! usr/bin/python

"""Pyg latin program that will take an input of an english word and translate it to pyg latin
    if the word starts with a vowel, it will take the word and add "ay" to it. Otherwise, it will
    take the first letter, truncate it, and put it in the end with "ay". """

#variable that will contain 'ay'
pyg = "ay"
runProgram = True

while(runProgram):
    runThis = raw_input("Would you like to run this application? Y or N: ")

    if(runThis == "Y" or runThis == "y"):
        #ask for input
        originalWord = raw_input("Please enter a word: ")

        #if statement will get lenght of the input and compare it to zero and check if the input is greater than 0
        if (len(originalWord) > 0 and originalWord.isalpha()):
            word = originalWord.lower()
            first = word[0]

            #nested if that will check if input starts with consonant
            if (first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u'):
                newWord = word + pyg
                print newWord
            else:
                newWord = word[1:] + word[0:1] + pyg
                print newWord
        else:
            print"There was now valid word inputed."
    if(runThis == "n" or runThis == "N"):
        print "Goodbye."
        runProgram = False

