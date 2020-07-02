from HTMLParser import HTMLParser

import requests

from question import Question

print("Welcome to Trivia \n")

topics = {"General Knowledge": "9", "Books": "10", "Film": "11", "Music": "12",
          "Musicals & Theaters": "13", "Television": "14", "Video Games": "15", "Board Games": "16",
          "Science & Nature": "17", "Computers": "18", "Math": "19", "Mythology": "20", "Sports": "21",
          "Geography": "22", "History": "23", "Politics": "24", "Arts": "25", "Celebrities": "26",
          "Animals": "27", "Vehicles": "28", "Comics": "29", "Gadgets": "30", "Cartoons": "32"}
user_topic = ''
user_score = 0
user_lives = 5

# user selects topic with error checking
print("Pick a topic: ")
for i in range(len(topics)):
    print(str(i + 1) + ") " + topics.keys()[i])

while True:
    try:
        user_topic = int(raw_input("Topic (1-" + str(len(topics)) + "): "))
        if user_topic < 1 or user_topic > len(topics):
            raise ValueError()
        break
    except ValueError:
        print("You must enter a whole number between 1 and " + str(len(topics)))
user_topic = str(topics[topics.keys()[user_topic - 1]])
print("\n")

# api call
response = requests.get("https://opentdb.com/api.php?amount=20&category=" + user_topic)
api = response.json()
questions_information = api["results"]

# question loop
question_num = 0;
while user_lives > 0 and question_num < 20:
    question_num += 1

    # unescape the questions and answers
    p = HTMLParser()
    question = p.unescape(questions_information[question_num]["question"])
    answer = p.unescape(questions_information[question_num]["correct_answer"])
    incorrect_answers = p.unescape(questions_information[question_num]["incorrect_answers"])

    q = Question(question, answer, incorrect_answers)
    result = q.ask_question()
    user_lives += result
    if result == 0:
        user_score += 1

# game ending
if user_lives > 0:
    print("Congrats! You finished the game with " + str(user_lives) + " lives and a score of " + str(user_score))
else:
    print("You failed with a score of " + str(user_score))
