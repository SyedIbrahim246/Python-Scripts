#Obtain input for name, age, and geneder.

name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Are you Male or Female? ")

#Convert the age input into an integer to perform mathematical operations.

age = int(age)
years1 = str(age-18)
years2 = str(18-age)

#Convert the gender input into lower case. Input of Male or male both can be used this way.

gender = gender.lower()
i = 1

#Conditional statements to filter the input by gender, and then determine if the person is an adult or a minor.

if gender == "male":
    if age >= 18:
        print(str(name) + " is an adult. He has been an adult for " + years1 + " years")
    else:
        print(str(name) +" is a minor.")

#The while loop is only incorporated for practice purpose. The above else statement is sufficient for printing that the person is a minor.

    while age < 18:
        if i == 1:
            print("He will be " + str(age + 1) + " in " + str(i) + " year.")
            i += 1
            age += 1
        if i > 1:
            print("He will be " + str(age + 1) + " in " + str(i) + " years.")
            i += 1
            age += 1

if gender == "female":
    if age >= 18:
        print(str(name) + " is an adult. She has been an adult for " + years1 + " years")
    else:
        print(str(name) + " is a minor.")

    while age < 18:
        if i == 1:
            print("She will be " + str(age + 1) + " in " + str(i) + " year.")
            i += 1
            age += 1
        if i > 1:
            print("She will be " + str(age + 1) + " in " + str(i) + " years.")
            i += 1
            age += 1

input("Press Enter to exit:")