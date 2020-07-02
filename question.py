import random


class Question:

    def __init__(self, question, answer, incorrect_answers):
        self.question = question
        self.answer = answer
        self.incorrect_answers = incorrect_answers
        self.all_answers = self.calc_all_answers()

    def calc_all_answers(self):
        answers = []
        answers.append(self.answer)
        for answer in self.incorrect_answers:
            answers.append(answer)
        random.shuffle(answers)
        return answers

    def ask_question(self):
        print(self.question)
        for i in range(len(self.all_answers)):
            print(str(i + 1) + ") " + self.all_answers[i])
        user_answer = -1
        while True:
            try:
                user_answer = int(raw_input("Answer (1-" + str(len(self.all_answers)) + "): "))
                if user_answer < 1 or user_answer > len(self.all_answers):
                    raise ValueError()
                break
            except ValueError:
                print("You must enter a whole number between 1 and " + str(len(self.all_answers)))

        if self.all_answers[user_answer - 1] != self.answer:
            print("Incorrect! The correct answer was " + self.answer + "\n")
            return -1
        else:
            print("Correct! \n")
            return 0
