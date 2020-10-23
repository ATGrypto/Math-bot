# Math-bot
print("Title of program: Math Revision")
print()
print("Please answer the following questions truthfully and you to test your math  skills!")
print("Please respond with an answer")
print()

multiplication_final = 0
multiplication1 = int(input("what is the answer for 5 x 5 x 5?"))
if multiplication1 == 125:
  print("Great!")
  multiplication_final += 1
else:
  print("Oops! That's incorrect! Try again")

multiplication2 = input("what is the answer for 4x x 2 + 21x?")
if multiplication2 == "29x":
  print("Great Job!")
  multiplication_final += 1
else:
  print("Oops! That's incorrect! Try again")

multiplication3 = int(input("what is the answer for 34-67+689+(69x2)?"))
if multiplication3 == 794:
  print("Yay! You got it correct!")
  multiplication_final += 1
else:
  print("Oops! That's incorrect! Try again") 

print("You got " + str(multiplication_final) + " / 3 . Hooray! You did it!")
