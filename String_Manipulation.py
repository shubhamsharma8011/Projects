# Encrypt a string by shifting each alphabet character one position forward. Example: "ABC" → "BCD" 
str=input("Enter the string: ")
out=""
for i in str:
    if i=="z":
        out=out+"a"
    elif i=="Z":
        out=out+"A"
    else:
        out=out+chr(ord(i)+1)
print("After shifting one position forward: ",out)


#Replace each vowel with the next vowel cyclically. Example: a → e, e → i, i → o, o → u, u → a 
word=input("Enter a word: ")
new_word=""
for i in word:
    if i=="a":
        new_word=new_word+"e"
    elif i=="e":
        new_word=new_word+"i"
    elif i=="i":
        new_word=new_word+"o"
    elif i=="o":
        new_word=new_word+"u"
    elif i=="u":
        new_word=new_word+"a"
    else:
        new_word=new_word+i
print("The word formed: ",new_word)


# Create a menu-driven program for string operations: 
# Count vowels ; Reverse string ; Check palindrome ; Replace a word ; Exit 
string=input("Enter the string: ")
choice=int(input("Enter the numbers given below to get the specific output:\n" \
    "===  To check number of vowels --> 1  ===\n" \
    "===  To reverse the string --> 2  ===\n" \
    "===  To check palindrome --> 3  ===\n" \
    "===  To replace a word --> 4  ===\n" \
    "===  EXIT --> 5  ===\n"  ))
if choice==1:
    vowels="aeiou"
    count=0
    for i in string:
        if i in vowels:
            count+=1
    print("Number of vowels: ",count)
if choice==2:
    print(string[::-1])
if choice==3:
    if string==string[::-1]:
        print("It is palindrome")
    else:
        print("It is no palindrome")
if choice==4:
    word_to_replace=input("Enter the word to replace: ")
    word_to_replace_with=input("Enter the word to replace with: ")
    print(string.replace(word_to_replace,word_to_replace_with))
if choice==5:
    print("EXIT")
    

#Input a sentence and display the shortest and longest words. 
line=input("Enter the sentence: ")
words=list(line.split())
longest=""
shortest=""
highest=0
lowest=1000
for word in words:
    length=len(word)
    if length>highest:
        longest=word
        highest=length
    if length<lowest:
        shortest=word
        lowest=length
print("Shortest: ",shortest)
print("Longest: ",longest)


#Create a program that checks whether a PAN number follows the pattern:
# five uppercase letters, four digits, and one uppercase letter. 
pan_number = input("Enter the PAN number: ")
upper = digit = upper2 = False
if len(pan_number)==10:
    if pan_number[:5].isupper():
        upper = True
    if pan_number[5:9].isdigit():
        digit = True
    if pan_number[9].isupper():
        upper2 = True
if upper and digit and upper2 == True:
    print("PAN number follows the pattern.")
else:
    print("PAN number does not follows the pattern.")


#Input a URL and extract its protocol, domain, and page path. 
url=input("Enter the URL: ")

index_protocol=url.index(":")

count=0
for i in range(len(url)):
    if url[i]=="/":
        count+=1
        if count==3:
            index_path=i

print("Protocol: ", url[:index_protocol])
print("Domain:", url[index_protocol+3:index_path])
print("Page path: ", url[index_path:])


#Create a program to generate initials from a full name.   
#Example: "Raj Kumar Singh" → "R.K.S." 
name=input("Enter the name:")
words=list(name.split())
initial=""
for name in words:
    initial+=name[0]+"."
print(initial)


# Input a paragraph and display the frequency of every word, ignoring case. 
paragraph=input("Enter the paragrph: ")
lower_words=paragraph.lower()
words=lower_words.split()
done=[]
for word in words:
    if word not in done:
        done.append(word)
        frequency=words.count(word)
        print(word,frequency)


#Check whether a text is a pangram —contains every letter from a to z. 
text=input("Enter the text:")

count=0

for i in "abcdefghijklmnopqrstuvwxyz":
    if i in text.lower():
        count+=1

if count==26:
    print("It is a pangram")
else:
    print("It is not a pangram")
        

#Create a program to mask all but the last four digits of a mobile number. 
number=input("Enter your phone number: ")
print("*"*(len(number)-4)+number[-4:])


# Input a date in DD-MM-YYYY format and display it as DD Month YYYY. 
date=input("Enter the date (DD-MM-YYYY): ")
mon=int(date[3:5])
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
new_date=date[:2]+" "+months[mon-1]+" "+date[-4:]
print(new_date)


#Write a function that accepts a string and returns the 
#Number of Uppercase letters, Lowercase letters, Digits, Spaces, and Special characters. 
s=input("Enter the string: ")
upper = lower = digit = spaces = special = 0
for i in s:
    if i.isupper():
        upper+=1
    if i.islower():
        lower +=1
    if i.isdigit():
        digit +=1
    if i == " ":
        spaces+=1
    if i in "!@#$%^&*(_+=)":
        special +=1
print("Number of Uppercase letters: ",upper)
print("Number of Lowercase letters: ",lower)
print("Number of Digits: ",digit)
print("Number of Spaces: ",spaces)
print("Number of Special characters: ",special)