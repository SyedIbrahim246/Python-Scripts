#Import question class from the Question file.

from Question import Question

#Define the test function which will be used to run the different kinds of tests.

final_score = 0
def test(questions):
    score = 0


    for question in questions:

        answer = input(question.prompt)
        if answer == question.answer:
            score +=1

        else:
            print("\nHa! Stupid!")

    if questions == questionsG:
        print("\nYou got " + str(score) + "/ " + str(len(questions)) + " correct! Lets see how you do with Maths now.\n")
        input("Press Enter to continue")

    elif questions == questionsM:
        print("\nYou got " + str(score) + "/ " + str(len(questions)) + " correct! Lets see how you do with Fortnite now.\n")
        input("Press Enter to continue")

    else:
        print("\nYou got " + str(score) + "/ " + str(len(questions)) + " correct!")


#Define the different questions that will be asked. G stands for general knowledge.

question_promptsG = [
    "\nWhat colour are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "\nWhat colour are bananas?\n(a) Orange\n(b) Magenta\n(c) Yellow\n\n",
    "\nWhat colour are strawberries?\n(a) Pink\n(b) Red\n(c) Black\n\n",
    "\nWhat do cows drink?\n(a) Milk\n(b) Water\n(c) Lemonade\n\n",
    "\nAre you dumb?\n(a) Yes\n(b) No\n\n"
    ]

#Define the questionsG class using imported questions class.

questionsG = [
    Question(question_promptsG[0], "a"),
    Question(question_promptsG[1], "c"),
    Question(question_promptsG[2], "b"),
    Question(question_promptsG[3], "b"),
    Question(question_promptsG[4], "a")
]

#Define the different maths questions that will be asked. M stands for maths.

question_promptsM =[
    "\n\nWhat's 8+5?\n(a) 10\n(b) 13\n(c) 15\n\n",
    "\nWhat's 7*4?\n(a) 74\n(b) 11\n(c) 28\n\n",
    "\nWhat's 72/6\n(a) 12\n(b) 16\n(c) 7\n\n",
]

#Define the questionsM class using imported questions class.

questionsM = [
    Question(question_promptsM[0], "b"),
    Question(question_promptsM[1], "c"),
    Question(question_promptsM[2], "a"),
]

#Define the different maths questions that will be asked. M stands for maths.

question_promptsF = [
    "\n\nWho is the real skibidi?\n(a) Jaz\n(b) Fadz\n(c) Mohammad\n\n",
    "\nWhat animal sound did Ehsaan mimic? \n(a) Cow \n(b) Cat \n(c) Duck\n\n",
    "\nWhy does vstarr not talk? \n(a) He doesn't want to\n(b) He has a lisp\n(c) He was bullied for talking\n\n"
]

questionsF = [
    Question(question_promptsF[0], "c"),
    Question(question_promptsF[1], "b"),
    Question(question_promptsF[2], "a"),
]

#Print statement to remind user that answers have to be input using the correct option instead of typing out the actual answer.
#Use the test function to run the tests.

print ("\nReminder: Please only use the the correct choice a, b, or c to answer the question. Writing out the answer will not be accepted and will result in not receiving a mark!")

test(questionsG)
test(questionsM)
test(questionsF)
#The prompt keeps the executable file open so the user can see the final result

input("Press Enter to exit")