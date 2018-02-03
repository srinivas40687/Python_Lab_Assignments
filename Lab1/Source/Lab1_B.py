Text = input("Enter a sentence")        #The user inputs the sentence of words


A = Text.split()        #Splits the sentence of words using " " and finds number of words in the sentence
length = len(A)
print(length)

print ("Middle word is: ")
def find_Middle_word(A):#Function to find the middle word in the sentence
 if (length % 2 == 0):
    print("[" + A[int(length / 2) - 1] + ", " + A[int(length / 2)] + "]")

 if (length % 2 == 1):
    print(A[int((length - 1) / 2)])

find_Middle_word(A)

print("Longest word is: ")        #Function to find the longest word in the sentence
def find_longest_word(A):
    longest_word = ''               #Initially the longest word is null
    for word in A:
        if len(word) > len(longest_word):        #Compares one word with the previous word in the sentence
            longest_word = word
    print (longest_word)


find_longest_word(A)


print("Sentence with reverse words is: ")
def reverseWord(Text):         #Function to reverse the words in the sentence



    # List Comprehension Technique
    ReversedWords = [word[::-1] for word in A]     # Reversing each word and creating a new list of words
    ReversedSentence = " ".join(ReversedWords)             # Joining the new list of words to make a new sentence
    return ReversedSentence

print(reverseWord(Text))