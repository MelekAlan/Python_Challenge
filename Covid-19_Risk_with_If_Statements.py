"""

Estimating the risk of death from coronavirus. Write a program that;

Takes "Yes" or "No" from the user as an answer to the following questions :

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).


"""


age = input("How old are you : ")
chronic = input("Do you have a severe chronic disease?(Yes/No):").strip().upper()
immune = input("Do you have a severe chronic disease? (Yes/No)").strip().upper()
cigarette = input("Are you a cigarette addict older than 75 years old?(Yes/No)").strip().upper()


if int(age) >= 75 or cigarette.startswith("Y") or immune.startswith("N") or chronic.startswith("Y") :
  print("You are in risky group!")
else :
  print("You are not in risky group!")
