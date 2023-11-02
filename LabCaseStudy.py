# Lorena Hendricks
# File name Lab Case Study
# This program is a case study for students who qualify for either the Dean's List or the Honor Roll
def qualify_student(firstname, lastname, gpa):
   if gpa >= 3.5:
       print(firstname,lastname, "qualifies for the dean's list.")
   elif gpa >= 3.25:
       print(firstname,lastname, "qualifies for the honor roll.")
   else:
       print(firstname, lastname, "does not qualify for either the dean's list or the honor roll.")
# Students:
qualify_student("Carly", "Hendricks", 3.8)
qualify_student("Emma", "Simpson", 2.9)
qualify_student("Daniel", "Sanchez", 2.3)
qualify_student("Gavin", "Brodrick", 3.2)
qualify_student("Sierra", "Smith", 3.25)

