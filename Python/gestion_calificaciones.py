#"""
#Sistema de Gestión de Calificaciones Académicas
#Permite calcular promedios de notas por materia y determinar aprobación/reprobación.
#Rango de calificación: 0.0 - 5.0
#Nota mínima de aprobación: 3.0
#"""
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
def notes(Value):
    lis = []
    i = 0
    while  Value > i:
        Note = float(input(f"Enter the note :  "))
        if Note >= 0 and Note <= 5:
            lis.append(Note)
            i += 1
        else:
            print("Number wrong in the range of 0 to 5")
    return lis

def mean1(grade):
    mean_note = sum(grade)/len(grade)
    return mean_note

def Rank(grade_total):
    if grade_total < 3:
        print(f"Disapproved with {grade_total:.2f}")
    if grade_total >= 3:
        print(f"Approved with {grade_total:.2f}")


print("-------------------Welcome--------------------")
print("-------------Rank from approved---------------")
print("-----------Grade of Zero to Five--------------")

dic = {}
clear()

while (True):
    print("--------------Insert the subject---------------")
    print(" 1) Pressed the number One from calculate his grade of subject")
    print(" 2) Pressed the number Two form exit")
    
    try:
        init = int(input("Enter the number: "))
        if init == 1:
            subject = input("Enter the subject: ")
            Value = int(input("Enter the number of notes: "))
            grade = notes(Value)
            grade_value = mean1(grade)
            Rank(grade_value)
            dic[subject] = grade_value
            input("\n Pressed Enter for continuoes")
            clear()
        elif init == 2:
            clear()
            print("-------Grades-------")
            for m,p in dic.items():
                print(f"{m} : {p:.2f}")
            print("--------Exiting-------")
            break
        else:
            print("Number wrong, enter again")
            input("\n Pressed Enter for continuoes")
            clear()
    
    except:
        print("Error")
        input("\n Pressed Enter for continuoes")
        clear()
