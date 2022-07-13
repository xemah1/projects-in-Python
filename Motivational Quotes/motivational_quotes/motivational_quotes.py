import os
import sys
import random

k = 0
with open(os.path.join(sys.path[0], "test.txt"), "r") as f: #test.txt file must be in the same folder as this .py file
   line = f.readline()
   while line : #counts how many lines there are
      k += 1
      line = f.readline()
   i = random.randint(0,k-1)
   k = 0
   f.seek(0)
   line = f.readline()
   while line and k != i : #reads a random line
      k += 1
      line = f.readline()
print()
print(line)
k = 0
i = 0
r = 0
for k in line : #counts the spaces between words and prints by adding 1 to that
   if k == "\"" : #word counter will be false if quotation format is not followed
      r += 1 #format is: "I am alive."
   if k == " " : #dont use unnecessary spaces after or before ( " ) mark
      i += 1 #anything outside of ("") marks will be ignored
   if r == 2 : #use exactly 2 quotation marks
      break #this is a code that can easily be broken without even touching the code
print("Word Count:",i+1)
k = 0
i = 0
r = 0
for k in line : #counts how many characters are used for the quotation
   if k == "\"" : #character counter will be false if quotation format is not followed
      r += 1 #format is: "I am alive."
   i += 1 #dont use unnecessary characters after or before ( " ) mark
   if r == 2 : #anything outside of ("") marks will be ignored
      break #use exactly 2 quotation marks
print("Character Count:",i) #this is a code that can easily be broken without even touching the code