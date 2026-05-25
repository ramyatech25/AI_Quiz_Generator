import os
import random
import time

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCORES_FILE = os.path.join(BASE_DIR, "scores.txt")


# Easy Questions
easy_questions = [
    {
        "question": "What is Python?",
        "options": ["A. Snake", "B. Programming Language", "C. Game", "D. Browser"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used for loops?",
        "options": ["A. loop", "B. for", "C. repeat", "D. next"],
        "answer": "B"
    },
    {
        "question": "Which data type stores text?",
        "options": ["A. int", "B. float", "C. string", "D. bool"],
        "answer": "C"
    },
    {
        "question": "Which function displays output?",
        "options": ["A. input()", "B. print()", "C. show()", "D. output()"],
        "answer": "B"
    }
]


# Medium Questions
medium_questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. define", "C. function", "D. def"],
        "answer": "D"
    },
    {
        "question": "What does AI stand for?",
        "options": ["A. Artificial Intelligence", "B. Auto Input", "C. Advanced Internet", "D. None"],
        "answer": "A"
    },
    {
        "question": "Which operator is used for multiplication?",
        "options": ["A. +", "B. *", "C. /", "D. %"],
        "answer": "B"
    },
    {
        "question": "Which function takes user input?",
        "options": ["A. print()", "B. output()", "C. input()", "D. scan()"],
        "answer": "C"
    },
    {
        "question": "Which data type stores decimal numbers?",
        "options": ["A. int", "B. float", "C. string", "D. bool"],
        "answer": "B"
    }
]


# Hard Questions
hard_questions = [
    {
        "question": "Which data type stores whole numbers?",
        "options": ["A. float", "B. string", "C. int", "D. list"],
        "answer": "C"
    },
    {
        "question": "Which loop is used for fixed iterations?",
        "options": ["A. while", "B. for", "C. loop", "D. repeat"],
        "answer": "B"
    },
    {
        "question": "Which keyword exits a loop?",
        "options": ["A. stop", "B. continue", "C. skip", "D. break"],
        "answer": "D"
    },
    {
        "question": "Which keyword skips one iteration?",
        "options": ["A. pass", "B. continue", "C. break", "D. skip"],
        "answer": "B"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. list", "B. tuple", "C. set", "D. dictionary"],
        "answer": "D"
    }
]
# Save Score
def save_score(name, score, total):

    with open(SCORES_FILE, "a") as file:
        file.write(f"{name} - Score: {score}/{total}\n")


# Select Difficulty
def choose_difficulty():

    print(YELLOW + "\nSelect Difficulty Level" + RESET)
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter choice: ")

    if choice == "1":
        return easy_questions

    elif choice == "2":
        return medium_questions

    elif choice == "3":
        return hard_questions

    else:
        print(RED + "Invalid Choice! Defaulting to Easy." + RESET)
        return easy_questions


# Quiz Function
def run_quiz():

    print(BLUE + "===================================")
    print("     Welcome to AI Quiz Generator")
    print("===================================" + RESET)

    name = input("Enter your name: ")

    questions = choose_difficulty()

    # Randomize Questions
    random.shuffle(questions)

    score = 0
    total = len(questions)

    # Quiz Loop
    for index, q in enumerate(questions, start=1):

        print(YELLOW + f"\nQuestion {index}:" + RESET)
        print(q["question"])

        for option in q["options"]:
            print(option)

        print(GREEN + "You have 20 seconds to answer!" + RESET)

        start_time = time.time()

        answer = input("Your Answer (A/B/C/D): ").upper()

        end_time = time.time()

        time_taken = end_time - start_time

        # Timer Check
        if time_taken > 20:
            print(RED + "Time Over!" + RESET)
            continue

        # Answer Validation
        if answer == q["answer"]:
            print(GREEN + "Correct Answer!" + RESET)
            score += 1

        else:
            print(RED + "Wrong Answer!" + RESET)
            print("Correct Answer is:", q["answer"])

    # Final Result
    print(BLUE + "\n===================================")
    print("           FINAL RESULT")
    print("===================================" + RESET)

    print(f"Player Name : {name}")
    print(f"Final Score : {score}/{total}")

    percentage = (score / total) * 100

    print(f"Percentage  : {percentage:.2f}%")

    if percentage >= 80:
        print(GREEN + "Result      : Excellent" + RESET)

    elif percentage >= 60:
        print(YELLOW + "Result      : Good" + RESET)

    elif percentage >= 40:
        print(YELLOW + "Result      : Average" + RESET)

    else:
        print(RED + "Result      : Needs Improvement" + RESET)

    print(BLUE + "===================================" + RESET)

    # Save Score
    save_score(name, score, total)

    print(GREEN + "Score saved successfully in scores.txt" + RESET)

    # Prevent Terminal Closing
    input("\nPress Enter to close the program...")


# Run Program
run_quiz()
