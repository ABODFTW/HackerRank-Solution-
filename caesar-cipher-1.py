import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):

	# Creating shifted chars list
	alphabets = ["a","b","c","d","e","f","g","h","i","j","k" ,"l" ,"m" , "n", "o", "p" ,"q" , "r" , "s","t" , "u" ,"v" ,"w" ,"x","y" ,"z"]

	v2_alphabets = []
	counter = 0
	if k > len(alphabets):
		k = k % len(alphabets)
	for i in alphabets:
		# this to prevent from out of index error 
		if counter + k >= len(alphabets):
			counter = 0
			for i in range(0 ,k):
				v2_alphabets.append(alphabets[counter])
				counter+=1
			break
		else :
			v2_alphabets.append(alphabets[counter + k])
		counter+=1

	keys_dic = dict(zip(alphabets,v2_alphabets))

	# Encoding Proccess 	
	encoded_string = ""

	for char in s:
		# this in case the letter is upper case or not in the alphabet 
		if char not in alphabets:
			# if it's upper case then 
			if char.isupper():
				coded_char = keys_dic[char.lower()]
				coded_char = coded_char.upper()
				encoded_string += coded_char
			else :
				encoded_string += char
		# or add it as is 
		else :
			encoded_string += keys_dic[char]

	return encoded_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())
	

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()