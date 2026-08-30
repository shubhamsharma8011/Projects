#Write a menu driven program, to diplay statistics of the users input(700 to 1500 words)
#number of words, most used word, number of spaces, number of vowels, most used vowel, number of symbols, it contains digits only, alphabets only or alphanumeric, it is lowercase or uppercase 

text=input("""Enter the text which should contain 700 to 1500 words:\n""")
number_of_words=len(text.split())

if number_of_words>700 and number_of_words<1500:
    print()
    choice=int(input("Enter the numbers given below to get the specific output:\n" \
    "===  To check number of words --> 1  ===\n" \
    "===  To check most used word --> 2  ===\n" \
    "===  To check number of spaces --> 3  ===\n" \
    "===  To check number of vowels --> 4  ===\n" \
    "===  To check most used vowel --> 5  ===\n" \
    "===  To check number of symbols --> 6  ===\n" \
    "===  To check it contains digits only, alphabets only or alphanumeric --> 7  ===\n" \
    "===  To check it is lowercase or uppercase --> 8  ===\n"))
    
    if choice==1:
        print("Number of words: ", number_of_words)

    if choice==2:
        words=text.lower().split()
        most_word=""
        highest=0
        for word in words:
            count=0
            for w in word:
                if word==w:
                    count+=1
            if count>highest:
                highest=count
                most_word=word
        print("Most used word:", most_word)
        print("Used:", highest, "times")

    if choice==3:
        number_of_spaces=0
        for character in text:
            if character==" ":
                number_of_spaces+=1
        print("Number of spaces: ", number_of_spaces)

    if choice==4:
        number_of_vowels=0
        for vowels in text:
            if vowels in 'aeiou':
                number_of_vowels+=1
        print("Number of vowels: ", number_of_vowels)

    if choice==5:
        vowels = "aeiou"
        most_vowel = ""
        highest = 0
        for vowel in vowels:
            count = 0
        for character in text.lower():
            if character == vowel:
                count += 1      
        if count > highest:
            highest = count
            most_vowel = vowel
        print("Most used vowel:", most_vowel)
        print("Used:", highest, "times")


    if choice==6:
        number_of_symbols=0
        for symbols in text:
            if symbols in '@#$%^&*()-+=[]|<>':
                number_of_symbols+=1
        print("Number of symbols: ", number_of_symbols)

    if choice==7:
        if text.isalpha():
            print("It contains only alphabets.")
        elif text.isdigit():
            print("It contains only digits.")
        else:
            print("It contains both alphabets and digits.")

    if choice==8:
        if text.islower():
            print("It has only the texts in lowercase.")
        elif text.isupper():
            print("It has only the texts in uppercase.")
        else:
            print("It has the texts in lowercase and also in uppercase.")


elif number_of_words<700:
    print("Invalid: Please enter the text more than 700 words")

else:
    print("Invalid: Please enter the text less than 1500 words")
