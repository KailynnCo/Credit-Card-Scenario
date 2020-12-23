#Your the most known hacker in the USA. who was able to get the credentials of someones credit card number. Unfortunately your friend is unable to read the credit card, due to loosing his glasses. 

#Write a program that reads a 16 positive integer for a credit card. It breaks it into a sequence of individual digits. For example, the input 16384 is displayed as : 1 6 3 8 4

#purpose of this program is to prove you can use strings, data types, list, and variables, relational operators.



print ("Please enter a 16 digit credit card number: ") #get the users input
Num = int(input())
NumberAsString= str(Num)
Lenght = len(NumberAsString)

#make sure they only enter positive
if Lenght < 16 :
  print (" I'm sorry but you have to enter 16 positive numbers, not anything less ")

#NumberAsString= str(Num) #turn it into a string so i can start seperating them 

#Lenght = len(NumberAsString) # define lenght 4

print (NumberAsString[0] + " " + NumberAsString[1] + " " + NumberAsString[2] + " " + NumberAsString[3] + " " + NumberAsString[4] + " " + NumberAsString[5] + " " + NumberAsString[6] + " " + NumberAsString[7] + " " + NumberAsString[8] + " " + NumberAsString[9] + " " + NumberAsString[10] + " " + NumberAsString[11] + " " + NumberAsString[12] + " " + NumberAsString[13] + " " + NumberAsString[14] + " " + NumberAsString[15] + " " + NumberAsString[16] + " ")  #print it out and use " " for spaces
