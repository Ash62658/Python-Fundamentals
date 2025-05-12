#Word count in a sentence

#get the sentence from user

s1 = input("Enter a sentence to count the words dont use comma or it will be a part of a word also use only one space between words : ")
list1 = s1.split(" ")
print(f"no. of words in the sentence is {len(list1)}")
