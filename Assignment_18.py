Score = int(input("Enter your score (0-100):"))
if(Score >= 40):
    print("Congratulation.You have passed the exam.\nStatus:PASS")

if(Score >= 90):
    print("You got (Grade):('A+')")

elif(Score >= 80):
    print("You got (Grade):('A')")

elif(Score >= 60):
    print("You got (Grade):('B')")

elif(Score >= 40):
    print("You got (Grade):('c')")

else:
    print("OOPS!! You have failed the exam. Better luck next time.\nStatus:FAIL")
  

