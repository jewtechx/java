quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "madrid"
    },"question5": {
        "question": "What is the capital of Portugal?",
        "answer": "lisbon"
    },"question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "bern"
    },"question7": {
        "question": "What is the capital of Austria?",
        "answer": "vienna"
    },
}

score = 0

for (key,value) in quiz.items():
    print(value["question"])
    answer = input("Answer is: ")
    if answer.lower() == value["answer"]:
        print("Correct👍✨!!")
        score = score + 1
        print("")
        print("")
        print("")
    else:
        print("Wrong😈!!")
        print("")
        print("")
        print("")

print(f"Your score is {score} out of 7")
print(f"That is {round(score / 7 * 100,1)} %")