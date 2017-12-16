phrase = "That Test to get into University"
print(phrase.upper())

print("Please be aware that if your answer is without a period mark at the end (a) it will be incorrect.")
print("If you correctly answer all 2 questions in this area you will aquire a perfect grade.")
print("If you receive less then 2 right in this area you will fail the test.")

print("1st Section Math")

print("Multiple Choice")

print("You have 5 minutes to read and complete this section.")

print("If 200 + 0 = 2000 what is 200 - 0?")

print("Chose:")
print("a. 2000\nb. 200\nc. 20\nd. 2\ne. 0")

while True:
    Answer = input("Choose 'a.' 'b.' 'c.' 'd.' or 'e.' all answers are final.")
   
    if Answer ==  "b.":
        break
    else:
        print("PyQuiz is reviewing your answer... Your answer is incorrect correct answer was: b.")

print("Question 2.")

print("What type of shape is below?")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("Chose:")
print("a. Dodecahedron\nb. Square\nc. Rhombicosidodecahedron\nd. Triangle\ne Rectangle")

while True:
    Answer2 = input("Choose 'a.' 'b.' 'c.' 'd.' 'e.'  all answers are final.")

    if Answer2 ==  "d.":
        break
    else:
        print("PyQuiz is reviewing your answer...Your answer is incorrect correct answer was: d.")

print("Congragulations you've completed the Math section!")

print("STOP. Do not continue until told to do so.")



print("Please continue into the Science section")
print("2nd section Science")

print("If you correctly answer all 6 questions correctly you will aquire a perfect grade.")
print("Do otherwise and be rewarded with a agonizing failure.")

print("True or Flase:")

print("You have 10 minutes to read and complete this section")

print("ToF 1 Topic: Human Anatomy: The femur is the longest bone in the human body.")
print("ToF 2 Topic: Elements: The chemical symbol for Tin is Sn.")
print("ToF 3 Topic: Chemistry: The chemical formula for ethanol is C₂H₅OH.")
print("ToF 4 Topic: Nature: Centipedes are considered insects.")
print("ToF 5 Topic: Human Anatomy: The aorta is a vein. ")
print("ToF 6 Topic: Optics: Red has a higher frequency light the Blue.")

while True:
    ToF1 = input("The femur is the longest bone in the human body is this True or False?")

    if ToF1 == "True.":
        break
    else:
        print("PyQuiz is reviewing your answer... Your answer is incorrect.")

while True:
    TrueorFalse2 = input("The chemical symbol for Tin is Sn is this True or False?")
    if TrueorFalse2 == "True.":
        break
    else:
        print("PyQuiz is reviewing your answer... Your answer is incorrect.")

while True:
    ToF3 = input("The chemical formula for ethanol is C₂H₅OH is this True or False.")
    if ToF3 == "True.":
       break
    else:
        print("That is incorrect the answer was, True.")

while True:
        ToF4 = input("Centipedes are considered insects, is this True or False?")
        if ToF4 == "False.":
            break
        else:
             print("The answer was False, okay?")


while True:
    ToF5 = input("The aorta is a vein id this True or False?")
    if ToF5 == "False.":
        break
    else:
        print("Mr. PyQuiz really needs a break so stop getting them incorrect.")

while True:
    ToF6 = input("Red has a higher frequency light the Blue is this True or False?")
    if ToF6 == "False.":
        break
    else:
        print("Seriously, again? Can you at least get one right? -Mr. PyQuiz")

print("Congragulations on finishing the test! You got accepted in to a total of 0 Universities!")
